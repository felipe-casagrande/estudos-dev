#include <stdio.h>

int mat [3][3];
int mat2 [3][3];
int mat3 [3][3];
int main(){

    //loop para criar a matriz 1

    printf("\nVamos comecar a digitar os valores para a primeira matriz!\n");
    for(int l =0;l<3;l++)
    {
        for(int c=0;c<3;c++)
        {
            printf("Digite um numero: ");
            scanf("%d",&mat[l][c]);
        }
    }
    printf("\nPrimeira matriz pronta\n");

    //loop para criar matriz 2

    printf("\nAgora serao os valores para a matriz 2...\n");
    for(int l =0;l<3;l++)
    {
        for(int c=0;c<3;c++)
        {
            printf("Digite um numero: ");
            scanf("%d",&mat2[l][c]);
        }
    }
    // loop para mostrar as matrizez
    printf("\nprimeira matriz!\n");
    for(int l =0;l<3;l++)
    {
        for(int c =0;c<3;c++)
        {
            printf("%4d",mat[l][c]);
        }
        printf("\n");
    }
    printf("\nSegunda matriz!\n");
    for(int l =0;l<3;l++)
    {
        for(int c =0;c<3;c++)
        {
            printf("%4d",mat2[l][c]);
        }
        printf("\n");
    }
    printf("\nAgora vamos somar elas..\n");
    for(int l=0;l<3;l++)
    {
        for(int c=0;c<3;c++)
        {
            mat3[l][c] = mat[l][c]+mat2[l][c];
        }
    }
    printf("\nMatriz Final!\n");
    for(int l =0;l<3;l++)
    {
        for(int c =0;c<3;c++)
        {
            printf("%4d",mat3[l][c]);
        }
        printf("\n");
    }
    return 0;
}
