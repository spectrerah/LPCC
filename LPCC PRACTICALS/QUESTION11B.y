%{
#include <stdio.h>
#include <ctype.h>
%}

%token STRING

%%

input:
    line
    ;

line:
    STRING {
        printf("Converted: %s\n", $1);
    }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    // Prompt the user to enter input
    printf("Please enter your text: ");
    return yyparse();
}
