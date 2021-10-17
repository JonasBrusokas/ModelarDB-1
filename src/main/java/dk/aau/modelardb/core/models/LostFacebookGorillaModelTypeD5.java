package dk.aau.modelardb.core.models;

import dk.aau.modelardb.core.DataPoint;

import java.util.List;

public class LostFacebookGorillaModelTypeD5 extends LostFacebookGorillaModelType {

    public LostFacebookGorillaModelTypeD5(int mtid, float errorBound, int lengthBound) {
        super(mtid, errorBound, lengthBound);
        this.abstractLostGorillaModelType = new AbstractLostGorillaModelType(mtid, errorBound, lengthBound, (float)5.0);
    }

}
