%{
#include <stdio.h>
#include <stdlib.h>

// Declare yytext for use in the parser
extern char* yytext;

void yyerror(const char *s);
int yylex(void);

%}

%token IDENTIFIER

%%

input:
    identifiers
    ;

identifiers:
    | identifiers IDENTIFIER { printf("Valid variable name: %s\n", yytext); }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    exit(1);
}

int main(void) {
    printf("Enter variable names (Ctrl+D to end):\n");
    yyparse();
    return 0;
}
