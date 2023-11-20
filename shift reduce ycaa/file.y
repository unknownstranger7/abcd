%{
    #include <stdio.h>
%}
%token PLUS
%token T
%token END
%%
start: E END { printf("Valid Expression\n"); };
E: E PLUS T {
    printf("Reduce: E -> E + T\n");
}
| T {
    printf("Shift: E -> T\n");
};
%%
#include <stdio.h>
#include <stdlib.h>
int yylex(void);
int main() {
    printf("Shift-Reduce Parsing\n");
    yyparse();
    return 0;
}
void yyerror(const char *msg) {
    fprintf(stderr, "Error: %s\n", msg);
}

