package dk.aau.modelardb.core.models;

public class LostFacebookGorillaModelTypeD25 extends LostFacebookGorillaModelType {

    public LostFacebookGorillaModelTypeD25(int mtid, float errorBound, int lengthBound) {
        super(mtid, errorBound, lengthBound);
        this.abstractLostGorillaModelType = new AbstractLostGorillaModelType(mtid, errorBound, lengthBound, (float)25.0);
    }

}
