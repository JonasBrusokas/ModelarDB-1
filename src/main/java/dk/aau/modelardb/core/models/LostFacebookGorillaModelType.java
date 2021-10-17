package dk.aau.modelardb.core.models;

import dk.aau.modelardb.core.DataPoint;

import java.util.List;

public class LostFacebookGorillaModelType extends ModelType {

    protected AbstractLostGorillaModelType abstractLostGorillaModelType;

    public LostFacebookGorillaModelType(int mtid, float errorBound, int lengthBound) {
        super(mtid, errorBound, lengthBound);
        abstractLostGorillaModelType = new AbstractLostGorillaModelType(mtid, errorBound, lengthBound, (float)0.0);
    }

    @Override
    public boolean append(DataPoint[] currentDataPoints) {
        return abstractLostGorillaModelType.append(currentDataPoints);
    }

    @Override
    public void initialize(List<DataPoint[]> currentSegment) {
        abstractLostGorillaModelType.initialize(currentSegment);
    }

    @Override
    public byte[] getModel(long startTime, long endTime, int samplingInterval, List<DataPoint[]> dps) {
        return abstractLostGorillaModelType.getModel(startTime, endTime, samplingInterval, dps);
    }

    @Override
    public Segment get(int tid, long startTime, long endTime, int samplingInterval, byte[] model, byte[] offsets) {
        return abstractLostGorillaModelType.get(tid, startTime, endTime, samplingInterval, model, offsets);
    }

    @Override
    public int length() {
        return abstractLostGorillaModelType.length();
    }

    @Override
    public float size(long startTime, long endTime, int samplingInterval, List<DataPoint[]> dps) {
        return abstractLostGorillaModelType.size(startTime, endTime, samplingInterval, dps);
    }

}
