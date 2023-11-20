%{
	#include<stdio.h>	
	int count=0;
%}
letters [a-zA-Z_]
digits [0-9]
whitespaces [ \t\n]
literals [""]	
assign [=]
para [{}()]

%%

int|float|switch|if|else|void { printf("\nkeyword:%s",yytext); count++;}	

{literals} { printf("\nliterals:%s",yytext); count++; }

{para} { printf("\nParanthesis:%s",yytext); count++; }

{digits} { printf("\ndigits:%s",yytext); count++;}

{letters}({letters}|{digits})* { printf("\nidentifier:%s",yytext); count++;}

{assign} { printf("\nassignment:%s",yytext); count++; }

">"|"<"|"<="|">="|"==" { printf("\nrelational:%s",yytext); count++;}

"\"".*"\"" { printf("\nwhole token:%s",yytext); count++; }
	
{whitespaces} ;

. { printf("\nothers:%s",yytext); count++; }

%%

int main(){
	yyin=fopen("ref.txt","r");
	yylex();
	fclose(yyin);
	printf("\nno of tokens:%d",count);
	return 0;
}

int yywrap(){
	return 1;
}
