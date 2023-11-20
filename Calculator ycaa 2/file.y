%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int yylex();
int power(int base, int exp) {
    int ret = 1;
    for (int i = 0; i < exp; i++) {
        ret = ret * base;
    }
    return ret;
}
%}

%token NUM
%left '+' '-'
%left '*' '/'
%right '^'
%%
calc: /* empty */
| calc expr '\n' { printf("Result: %d\n", $2); }
;
expr: NUM { $$ = $1; }
| expr '+' expr { $$ = $1 + $3; }
| expr '-' expr { $$ = $1 - $3; }
| expr '*' expr { $$ = $1 * $3; }
| expr '/' expr {
    if ($3 == 0) {
        yyerror("Division by zero");
        $$ = 0;
    }else {
        $$ = $1 / $3;
    }
}
| expr '^' expr { $$ = power($1, $3); }
;
%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n");
}
int main() {
    yyparse();
    return 0;
}
