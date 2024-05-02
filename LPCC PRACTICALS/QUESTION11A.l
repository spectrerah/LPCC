%{
#include "QUESTION11A.tab.h"
%}

%%
[a-zA-Z_][a-zA-Z_0-9]*  { return IDENTIFIER; }
.                      { yyerror("Invalid input"); }
%%

int yywrap(void) {
    return 1;
}
