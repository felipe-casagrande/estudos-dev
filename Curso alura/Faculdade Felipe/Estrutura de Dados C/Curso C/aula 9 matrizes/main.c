#include <stdio.h>
int mat [2][3];
int main()
{
    // para i = linha ; j = coluna
    // para cada linha eu faço um loop interno para receber os valores das colunas  
    // for para atribuir valores as linhas e colunas
    
    for(int i=0;i<2;i++)       // começa de 0, vai ate 2 pulando de 1 em 1 
    {
        for(int j=0;j<3;j++)
        {
            printf("Digite um numero: ");
            scanf("%d",&mat[i][j]);
        }
    }


    // for para mostrar os valores da matriz

     for(int i=0;i<2;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("\nOs valores de mat[%d][%d] = %d ",i,j,mat[i][j]);
        
        }
    }
    return 0;
}