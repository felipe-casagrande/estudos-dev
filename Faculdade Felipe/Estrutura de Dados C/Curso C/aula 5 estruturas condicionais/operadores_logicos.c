#include <stdio.h>


// && é igual o and do python
// || é igual o or em python
// ! operador logico NÃO, exemplo como se fosse um if not em python, !condição seria como um if not condicao
int main()
{
    int a,b,c;
    printf("Digite um numero: ");
    scanf("%d",&a);
    printf("Digite um numero: ");
    scanf("%d",&b);
    printf("Digite um numero: ");
    scanf("%d",&c);
    
    if(a==b && b==c)
    { 
        printf("a,b,c tem valores iguais!");   
    }   
    else
    {
        printf("nao possui valores iguais");
    }
    return 0;
}
    
 