%{
#include <stdio.h>
FILE *a_code;
FILE *a_comm;
%}

%%
[a-zA-Z ]* {fprintf(a_code,"%s",yytext); }


"//".* { fprintf(a_comm, "\n%s", yytext); }  // single-line

"\"".*"\"" { fprintf(a_code, "%s", yytext); }  // quotes- whole token

"/*".*|"*/" { fprintf(a_comm, "\n%s", yytext); }  // multiline

.*"*/" { fprintf(a_comm, "\n%s", yytext); }  // multiline

. { fprintf(a_code, "%s", yytext); }

%%

int main(){
    yyin = fopen("a_ref.txt", "r");
    if (!yyin) {
        perror("Error opening input file");
        return 1;
    }
    a_code = fopen("input.c", "w");
    a_comm = fopen("Comments.txt", "w");
    if (!a_code || !a_comm) {
        perror("Error opening output files");
        fclose(yyin);
        return 1;
    }

    yylex();

    fclose(yyin);
    fclose(a_code);
    fclose(a_comm);
    return 0;
}

int yywrap(){
    return 1;
}


