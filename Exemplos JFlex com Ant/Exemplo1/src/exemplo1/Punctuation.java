package exemplo1;

// Token de sinais de pontuação
public class Punctuation extends Token {
    public final Tag pu;

    public Punctuation(Tag pu) {
        super(Tag.PUNCTUATION);
        this.pu = pu;
    }

    @Override
    public String toString() {
        return "RELOP: <" + this.tag + ",\"" + this.pu + "\">";
    }
}