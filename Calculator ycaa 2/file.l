%{
    #include <stdio.h>
    #include <math.h>
    #include "file.tab.h"
%}
%%
[0-9]+ { yylval = atoi(yytext); return NUM; }
"+" { return '+'; }
"-" { return '-'; }
"*" { return '*'; }
"/" { return '/'; }
"^" { return '^'; }
\n { return '\n'; }
[ \t] ; // Ignore whitespace
. { printf("Invalid character: %s\n", yytext); }
%%
int yywrap() {
    return 1;
}
