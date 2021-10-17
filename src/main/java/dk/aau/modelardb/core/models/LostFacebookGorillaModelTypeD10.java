package dk.aau.modelardb.core.models;

public class LostFacebookGorillaModelTypeD10 extends LostFacebookGorillaModelType {

    public LostFacebookGorillaModelTypeD10(int mtid, float errorBound, int lengthBound) {
        super(mtid, errorBound, lengthBound);
        this.abstractLostGorillaModelType = new AbstractLostGorillaModelType(mtid, errorBound, lengthBound, (float)10.0);
    }

}
