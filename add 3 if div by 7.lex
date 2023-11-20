%{
#include <stdio.h>
int num;
%}

%%
[0-9]+ {
    num = atoi(yytext); // Convert matched text to an integer
    if (num % 7 == 0) {
        printf("%d is divisible by 7", num);
        num += 3;
	printf("\nafter adding 3 number is : %d",num);
    } else{
	    printf("\n%d is not divisible by 7",num);
    }
}

.|\n {
    // Ignore other characters
}

%%

int main() {	
    printf("enter the number : ");
    yylex();
    return 0;
}

int yywrap(){
	return 1;
}
