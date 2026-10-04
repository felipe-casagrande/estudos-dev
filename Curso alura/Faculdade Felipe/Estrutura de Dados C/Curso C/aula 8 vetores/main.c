#include <stdio.h>
int v[4];
float v1[3];
int main()
{
    v[0] = 45;
    v[1] = 78;
    v[2] = 9;
    v[3] = 5;

    for(int i=0; i<3;i++)
    {
        printf("digite um valor:  ");
        scanf("%f",&v1[i]);
    }

    // adicionando valores ao vetor v1
    for(int i=0;i<3;i++)
    {
        printf("\nO valor de v1[%d] = %.1f",i,v1[i]);
    } 

    for(int i=0; i<4;i++)
    {
        printf("\nO valor de v na posicao '%d' vale: %d", i,v[i]);
    }
    return 0;
}
