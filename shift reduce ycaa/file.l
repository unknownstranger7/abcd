%{
    #include "file.tab.h"
%}
%%
[Tt] { return T; }
\+ { return PLUS; }
\n { return END; }
. { /* Ignore other characters */ }
%%
int yywrap() {
    return 1;
} 

