package exemplo1;

public class MathOp extends Token{
    public final Tag mo;

    public MathOp(Tag mo) {
        super(Tag.MATHOP);
        this.mo = mo;
    }

    @Override
    public String toString() {
        return "RELOP: <" + this.tag + ",\"" + this.mo + "\">";
    }
}

