%{
#include "QUESTION11B.tab.h"
#include <ctype.h>
%}

%%
[a-z]+ { 
    for (int i = 0; i < yyleng; i++) {
        yytext[i] = toupper(yytext[i]); 
    }
    yylval = yytext;
    return STRING; 
}

[A-Z]+ {
    for (int i = 0; i < yyleng; i++) {
        yytext[i] = tolower(yytext[i]); 
    }
    yylval = yytext;
    return STRING; 
}

[a-zA-Z]+ {
    for (int i = 0; i < yyleng; i++) {
        if (isupper(yytext[i])) {
            yytext[i] = tolower(yytext[i]);
        } else {
            yytext[i] = toupper(yytext[i]);
        }
    }
    yylval = yytext;
    return STRING; 
}

.|\n     { 
    yylval = yytext;
    return STRING; 
}
%%

int yywrap() {
    return 1;
}
