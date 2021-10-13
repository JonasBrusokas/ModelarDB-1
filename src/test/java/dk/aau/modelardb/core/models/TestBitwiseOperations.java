package dk.aau.modelardb.core.models;

import static dk.aau.modelardb.core.models.LostFacebookGorillaModelType.*;

public class TestBitwiseOperations {

    public static void testTwo(Object value1, Object value2) {
        if (value1.equals(value2)) {
            System.out.println(value1.toString() + " equals " + value2.toString());
        } else {
            System.out.println(value1.toString() + " DOES NOT EQUAL " + value2.toString());
        }
    }

    public static void main(String[] args) {

        // getMask tests
        testTwo(getMask(0), 0);
        testTwo(getMask(1), 0x400000);
        testTwo(getMask(3), 0x700000);

        System.out.println(" >>> getFloatExponent");

        // getFloatExponent tests
        testTwo(getFloatExponent((float) 0.5), -1);
        testTwo(getFloatExponent((float)-0.5), -1);
        testTwo(getFloatExponent((float) 0.25), -2);
        testTwo(getFloatExponent((float) 128), 7);
        testTwo(getFloatExponent((float) 256), 8);
        testTwo(getFloatExponent((float)-256), 8);

        System.out.println(" >>> binaryOps");

        // Testing some binary operations
        testTwo(0x80000001 & 0x7fffffff, 1);
    }

}
