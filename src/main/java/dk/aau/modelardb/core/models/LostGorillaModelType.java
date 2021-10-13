/* Copyright 2018 The ModelarDB Contributors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package dk.aau.modelardb.core.models;

import dk.aau.modelardb.core.DataPoint;
import dk.aau.modelardb.core.utility.BitBuffer;

import java.util.List;

// Read about Gorilla: https://blog.acolyer.org/2016/05/03/gorilla-a-fast-scalable-in-memory-time-series-database/

class BitwiseOperations {

    static int log2floor(float number) {
        double v = Math.log(number) / Math.log(2);
        return (int) ((v < 0) ? Math.ceil(v) : Math.floor(v));
    }

    static int getFloatExponent(float number) {
        if (number == 0.0) return 0;

        int bits = Float.floatToRawIntBits(number);
        int sign = ((bits >> 31) == 0) ? 1 : -1;
        int exponent = ((bits >> 23) & 0xff);
        int mantissa = (exponent == 0) ?
                (bits & 0x7fffff) << 1 :
                (bits & 0x7fffff) | 0x800000;

//        int exponentSign = (exponent / 0x80 == 0) ? 1 : -1;
//        int exponentSignedValue = exponentSign * (exponent % 0x80);

        int exponentSignedValue = exponent - 0x7f;
        return (exponentSignedValue);
    }

    // This will leave 'digitsToNotMask' digits unmasked (with 1, instead of 0)
    static int getMask(int digitsToNotMask) {
        return 0x007fffff ^ (0x007fffff >> digitsToNotMask);
    }

    //    https://stackoverflow.com/questions/24273994/how-do-you-get-the-mantissa-of-a-float-in-java
    public static double getMantissa(double x) {
        int exponent = Math.getExponent(x);
        return x / Math.pow(2, exponent);
    }
}

//The implementation of this model type is based on code published by Michael Burman
// under the Apache2 license. LINK: https://github.com/burmanm/gorilla-tsc

// Attention, we found a lazy Gorilla with memory loss
class LostFacebookGorillaModelType extends ModelType {

    private float actualErrorBound;

    /** Constructors **/
    LostFacebookGorillaModelType(int mtid, float errorBound, int lengthBound) {
        super(mtid, errorBound, lengthBound);
    }

    // for float (32bit precision)
    // SIGN (31) - EXPONENT (30-23) - FRACTION (22-0)
    // if (leadingZeros >= 9) // SIGN and EXPONENT are same
    // We can then use the error bound to see how many values we can drop

    /** Public Methods **/
    @Override
    public boolean append(DataPoint[] currentDataPoints) {

        BitwiseOperations.getFloatExponent(2);

        if (this.currentSize == this.lengthBound) {
            return false;
        }

        if (this.currentSize == 0) {
            float firstValue = currentDataPoints[0].value;
            this.actualErrorBound = (float) Math.floor(firstValue/100*errorBound);
            int errorBoundExponent = BitwiseOperations.log2floor(this.actualErrorBound);

            this.lastVal = Float.floatToIntBits(firstValue);
            this.lastValFloat = firstValue;
            this.compressed.writeBits(lastVal, Integer.SIZE);
            for (int i = 1; i < currentDataPoints.length; i++) {
                compress(currentDataPoints[i].value);
            }
        } else {
            for (DataPoint dp : currentDataPoints) {
                compress(dp.value);
            }
        }
        this.currentSize += 1;
        return true;
    }

    @Override
    public void initialize(List<DataPoint[]> currentSegment) {
        this.currentSize = 0;
        this.compressed = new BitBuffer(4 * this.lengthBound);
        this.storedLeadingZeros = Integer.MAX_VALUE;
        this.storedTrailingZeros = 0;

        for(DataPoint[] dataPoints : currentSegment) {
            this.append(dataPoints);
        }
    }

    @Override
    public byte[] getModel(long startTime, long endTime, int samplingInterval, List<DataPoint[]> currentSegment) {
        return this.compressed.array();
    }

    @Override
    public Segment get(int tid, long startTime, long endTime, int samplingInterval, byte[] model, byte[] offsets) {
        return new FacebookGorillaSegment(tid, startTime, endTime, samplingInterval, model, offsets);
    }

    @Override
    public int length() {
        return this.currentSize;
    }

    @Override
    public float size(long startTime, long endTime, int samplingInterval, List<DataPoint[]> dps) {
        if (this.currentSize == 0) {
            return Float.NaN;
        } else {
            return this.compressed.size();
        }
    }

    /** Private Methods **/
    private void compress(float value) {
        int curVal = Float.floatToIntBits(value);
        int xor = curVal ^ this.lastVal;

        int leadingZeros = Integer.numberOfLeadingZeros(xor);
        int trailingZeros = Integer.numberOfTrailingZeros(xor);

//        int unsignedLeadingZeros = Integer.numberOfLeadingZeros(xor & 0x7fffffff);
//        if (unsignedLeadingZeros >= 9) {
//            // Special case
//            int digitsNotToMask = getFloatExponent(curVal) - log2floor(this.actualErrorBound);
//            if (digitsNotToMask < 0) digitsNotToMask = 0;
//            xor = xor & getMask(digitsNotToMask);
//        }

        // Potentially smelly? We would like to avoid
        if (Math.abs(value - this.lastValFloat) <= this.actualErrorBound) {
            xor = 0;
        }

        if (xor == 0) {
            // The previous value is exactly the same
            this.compressed.writeBit(false);
        } else {
            //Computes the number of leading and trailing zeros that it might be necessary to store

            if(leadingZeros >= 32) {
                leadingZeros = 31;
            }
            this.compressed.writeBit(true);

            if (leadingZeros >= this.storedLeadingZeros && trailingZeros >= this.storedTrailingZeros) {
                //Stores only the significant bits
                this.compressed.writeBit(false);
                int significantBits = 32 - this.storedLeadingZeros - this.storedTrailingZeros;
                this.compressed.writeBits(xor >>> this.storedTrailingZeros, significantBits);
            } else {
                //Stores a new number of leading zero bits before the significant bits
                this.compressed.writeBit(true);
                this.compressed.writeBits(leadingZeros, 5);

                int significantBits = 32 - leadingZeros - trailingZeros;
                this.compressed.writeBits(significantBits, 6);
                this.compressed.writeBits(xor >>> trailingZeros, significantBits);

                this.storedLeadingZeros = leadingZeros;
                this.storedTrailingZeros = trailingZeros;
            }
        }
        this.lastVal = curVal;

        if (!(Math.abs(value - this.lastValFloat) <= this.actualErrorBound)) {
            this.lastValFloat = value;
        }
    }

    /** Instance Variables **/
    private BitBuffer compressed;
    private int lastVal;
    private float lastValFloat;
    private int currentSize;
    private int storedLeadingZeros;
    private int storedTrailingZeros;
}


// TODO: consider extending from FacebookGorillaSegment
class LostFacebookGorillaSegment extends Segment {

    /** Constructors **/
    LostFacebookGorillaSegment(int tid, long startTime, long endTime, int samplingInterval, byte[] model, byte[] offsets) {
        //Unlike length(), capacity() is not impacted by changes to the segment's start time
        super(tid, startTime, endTime, samplingInterval, offsets);
        this.values = decompress(model, super.capacity());
    }

    /** Public Methods **/
    @Override
    public float min() {
        float min = Float.MAX_VALUE;
        int inc = getGroupSize();
        int init = inc * getTemporalOffset() + getGroupOffset();
        int length = init + inc * this.length();
        for (int index = init; index < length; index += inc) {
            min = Float.min(min, this.values[index]);
        }
        return min;
    }

    @Override
    public float max() {
        float max = -Float.MAX_VALUE;
        int inc = getGroupSize();
        int init = inc * getTemporalOffset() + getGroupOffset();
        int length = init + inc * this.length();
        for (int index = init; index < length; index += inc) {
            max = Float.max(max, this.values[index]);
        }
        return max;
    }

    @Override
    public double sum() {
        double acc = 0;
        int inc = getGroupSize();
        int init = inc * getTemporalOffset() + getGroupOffset();
        int length = init + inc * this.length();
        for (int index = init; index < length; index += inc) {
            acc += this.values[index];
        }
        return acc;
    }

    /** Protected Methods **/
    @Override
    protected float get(long timestamp, int index) {
        return this.values[index];
    }

    /** Private Methods **/
    private float[] decompress(byte[] values, int length) {
        float[] result = new float[length];
        BitBuffer bitBuffer = new BitBuffer(values);

        int storedLeadingZeros = Integer.MAX_VALUE;
        int storedTrailingZeros = 0;
        int lastVal = bitBuffer.getInt(Integer.SIZE);
        result[0] = Float.intBitsToFloat(lastVal);

        for (int i = 1; i < length; i++) {
            if (bitBuffer.readBit()) {
                if (bitBuffer.readBit()) {
                    //New leading and trailing zeros
                    storedLeadingZeros = bitBuffer.getInt(5);
                    byte significantBits = (byte) bitBuffer.getInt(6);
                    if (significantBits == 0) {
                        significantBits = 32;
                    }
                    storedTrailingZeros = 32 - significantBits - storedLeadingZeros;
                }

                int value = bitBuffer.getInt(32 - storedLeadingZeros - storedTrailingZeros);
                value <<= storedTrailingZeros;
                value = lastVal ^ value;
                lastVal = value;
                result[i] = Float.intBitsToFloat(lastVal);
            } else {
                result[i] = Float.intBitsToFloat(lastVal);
            }
        }
        return result;
    }

    /** Instance Variables **/
    private final float[] values;
}
