package exemplo1;

// Rótulos para as marcas
public enum Tag {
    EOF, NUMBER, ID,
    RELOP, IF, THEN, ELSE,
    LT, LE, EQ, NE, GT, GE, PROGRAM,
    WHILE, FOREACH, FUNCTION, END,
    PUNCTUATION, LK, RK, LP, RP, SC,
    CM , MATHOP, ADD, SUB, MULT, DIV,
    RDIV, INCR, DECR, DIF, DEQ
}

// PUNCTUATION : sinais de pontuação
// LK : left key (chaves esquerda)
// RK : right key (chaves direita)
// LP : left parentheses (parêntese esquerdo)
// RP : right parentheses (parêntese direito)
// SC : semicolon (ponto e virgula)
// CM : common (vírgula)
// ADD : addition (adição)
// SUB : subtraction (subtração)
// MULT : multiplication (multiplicação)
// DIV : division (divisão)
// RDIV : resto of division (resto da divisão)
// INCR : increment (incremento)
// DECR : decrement (decremento)
// DIF : diffent (diferente)
// DEQ : double equal (igual a)
