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
import dk.aau.modelardb.core.utility.Static;

import java.io.Serializable;
import java.util.Iterator;
import java.util.List;

// ModelType is for compressing the data
public abstract class ModelType implements Serializable {

    /** Constructors **/
    public ModelType(int mtid, float errorBound, int lengthBound) {
        this.mtid = mtid;
        this.errorBound = errorBound;
        this.lengthBound = lengthBound;
    }

    /** Public Methods **/

    // Returns true if managed to get within errorBound
    // currentDataPoints - one DataPoint per group.
    // In the configuration file you can set groups to be of 1 (.conf)
    
    // IN OUR CASE: currentDataPoints[0] is relevant
    // You get datapoints one at a time
    abstract public boolean append(DataPoint[] currentDataPoints);
    
    // [Lifecycle]
    // 1. initialize(...)
    // 2. append(...) until false
    // 3. size(...) or length()
    // 5. loop to 1.

    // I shouldn't be worrying about the segments
    abstract public void initialize(List<DataPoint[]> currentSegment);
    
    // 
    abstract public byte[] getModel(long startTime, long endTime, int samplingInterval, List<DataPoint[]> dps);
    
    // get(...) - used to reconstruct the model from disk
    abstract public Segment get(int tid, long startTime, long endTime, int samplingInterval, byte[] model, byte[] offsets);
    
    // Dimensionality of the subseries
    abstract public int length();

    // Size in bytes for the subsequence
    // TODO: why float? :D 
    abstract public float size(long startTime, long endTime, int samplingInterval, List<DataPoint[]> dps);
    // IMPL: getModel.length

    // tsA - "decompressed"
    // tsB - "raw"
    public boolean withinErrorBound(float errorBound, Iterator<DataPoint> tsA, Iterator<DataPoint> tsB) {
        boolean allWithinErrorBound = true;
        while (allWithinErrorBound && tsA.hasNext() && tsB.hasNext()){
            allWithinErrorBound = Static.percentageError(tsA.next().value, tsB.next().value) < errorBound;
        }
        return allWithinErrorBound;
    }

    final public float compressionRatio(long startTime, long endTime, int samplingInterval, List<DataPoint[]> dps, int gaps) {
        //     DPs tid: int, ts: long, v: float
        // Segment tid: int, start_time: long, end_time: long, mtid: int, model: bytes[], gaps: bytes[]
        //4 + 8 + 4 = 16 * data points is reduced to 4 + 8 + 8 + 4 + sizeof model + sizeof gaps
        return (16.0F * this.length()) / (24.0F + this.size(startTime, endTime, samplingInterval, dps) + (4.0F * gaps));
    }

    final public float unsafeSize() {
        //Computes the size without providing the model type with the information for it to verify the precision of its model
        return this.size(0L, 0L, 0, new java.util.ArrayList<>());
    }

    /** Instance Variables **/
    public final int mtid;
    public final float errorBound;
    public final int lengthBound;
}
