/**
 * Analisador léxico para expressões simples
 */
package exemplo1;

%%

%class Lexer
%public
%unicode
%debug
%standalone
%line
%column
%type Token

%eofval{
    return new Token(Tag.EOF);
%eofval}

%eof{
    System.out.println("Analise léxica terminada com sucesso!");
%eof}

%{
// Macros
%}
delim	= [\ \t\n]
ws		= {delim}+
letter	= [A-Za-z]
digit	= [0-9]
id		= {letter}({letter}|{digit})*
number	= {digit}+(\.{digit}+)?(E[+-]?{digit}+)?

%%
/* Regras e ações */
{ws}		{ /* ignorar */ }
if			{ return new Token(Tag.IF); }
then		{ return new Token(Tag.THEN); }
else		{ return new Token(Tag.ELSE); }
program     { return new Token(Tag.PROGRAM);}
while     { return new Token(Tag.WHILE);}
foreach     { return new Token(Tag.FOREACH);}
function     { return new Token(Tag.FUNCTION);}
end     { return new Token(Tag.END);}


{id}		{ return new Id(yytext()); }
{number}	{ return new Num(Double.parseDouble(yytext())); }
"<"			{ return new Relop(Tag.LT);}
"<="		{ return new Relop(Tag.LE);}
"="			{ return new Relop(Tag.EQ);}
"<>"		{ return new Relop(Tag.NE);}
">"			{ return new Relop(Tag.GT);}
">="		{ return new Relop(Tag.GE);}
"!="		{ return new Relop(Tag.DIF);}
"=="		{ return new Relop(Tag.DEQ);}
"{"		{ return new Punctuation(Tag.LK);}
"}"		{ return new Punctuation(Tag.RK);}
"("		{ return new Punctuation(Tag.LP);}
")"		{ return new Punctuation(Tag.RP);}
";"		{ return new Punctuation(Tag.SC);}
","		{ return new Punctuation(Tag.CM);}
"+"		{ return new MathOp(Tag.ADD);}
"-"		{ return new MathOp(Tag.SUB);}
"*"		{ return new MathOp(Tag.MULT);}
"/"		{ return new MathOp(Tag.DIV);}
"%"		{ return new MathOp(Tag.RDIV);}
"++"		{ return new MathOp(Tag.INCR);}
"--"		{ return new MathOp(Tag.DECR);}


/* Qualquer outro - gerar erro */
.		    { throw new Error("Símbolo ilegal <" + yytext() +
                "(" + (int)(yytext().charAt(0)) + ")" + ">"); }
