#include <stdio.h>
int numero = 5;    // para saber o fatorial de um numero, muda aqui
int fatorial = 1;

int main(){
    if(numero>=0)
    {
        for (int i = 1; i <= numero; ++i){
        fatorial *= i;
        }
        printf("O fatorial de %d vale %d",numero,fatorial);
    }
    else {
        printf("Nao pode ser realizado de numeros negativos!\n");

    }
    return 0;
}
