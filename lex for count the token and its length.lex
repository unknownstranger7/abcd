%{
#include <stdio.h>
int count=0;
%}
whitespace [ \t\n]
%%
[a-zA-Z][a-zA-Z0-9_]*|"==" { 
    printf("\nWord: %s (Length: %d)", yytext, yyleng);
	count++;
}

"\"".*"\"" { printf("\nwhole token: %s (Length: %d)",yytext,yyleng);  count++;}

{whitespace} ;

. { printf("\nother:%s (length:%d)",yytext,yyleng); count++; }   

%%

int main() {
    yyin = fopen("ref.txt", "r");
    yylex();
    fclose(yyin);
    printf("No of Tokens:%d",count);
    return 0;
}

int yywrap(){
	return 1;
}
