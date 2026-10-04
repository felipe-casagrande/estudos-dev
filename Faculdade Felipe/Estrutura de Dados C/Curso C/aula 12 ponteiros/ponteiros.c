#include <stdio.h>
// para criar ponteiros, criar do mesmo tipo da variavel e colocar um * antes, como int*p, depois colocar p = &variavel
int *p;
int val = 5;


int main(){
    p = &val;
    printf("o valor apontado por p vale: %d",*p);
    return 0;
}

