#include <stdio.h>
int main()
{
    printf("\nlaco while\n");
    int a = 0;
   
    while(a<5)
    {
        printf("\nVariavel 'a' vale: %d",a);
        a++; // a= a+1
    }
    printf("\nlaco FOR\n");

    for(int i =0; i<4 ; i++)
    //for (inicialização ; teste; incremento)
    {
        printf("\nA variavel 'i' vale: %d",i);
    }
    return 0;
}