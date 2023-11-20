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
"m" { return 'm'; }
\n { return '\n'; }
[ \t] ; // Ignore whitespace
. { printf("Invalid character: %s\n", yytext); return 0; } // Return 0 for invalid characters
%%

int yywrap() { 
    return 1;
}
