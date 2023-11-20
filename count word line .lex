%{
#include <stdio.h>
int charCount = 0;
int wordCount = 0;
int lineCount = 1;
%}

%%
\n { 
    lineCount++;
    wordCount++;
}

" " {
    // Count whitespace as word separators
    wordCount++;
}

[ \t]+ {
    // Count whitespace as word separators
    charCount += yyleng;
    wordCount++;
}

. {
    charCount++;
}

%%

int main() {
    yyin = fopen("input.txt", "r");
    if (!yyin) {
        perror("Error opening input file");
        return 1;
    }

    yylex();

    fclose(yyin);

    printf("Number of characters: %d\n", charCount);
    printf("Number of words: %d\n", wordCount);
    printf("Number of lines: %d\n", lineCount);

    return 0;
}

int yywrap() {
    return 1;
}
