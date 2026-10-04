#include <stdio.h>
#include <stdlib.h>

struct Cordenada{
    float x;
    float y;
};
typedef struct Cordenada Cordenada;

int main(){
    int n;
    printf("Digite quantas coordenadas ira fazer: ");
    scanf("%d",&n);
    Cordenada *pontos = (Cordenada*)malloc(n*sizeof(Cordenada));// Aloca dinamicamente memória para n  coordenadas/ Crie um ponteiro chamado pontos que aponta para um espaço de memória suficiente para guardar n coordenadas."
    
    
    for(int i = 0; i<n;i++)
    {
        
        printf("\nCoordenada %d- digite o valor de x: ",i+1);
        scanf("%f",&pontos[i].x);
        printf("\nCoordenada %d- digite o valor de y: ",i+1);
        scanf("%f",&pontos[i].y);
    }
    for(int i = 0;i<n;i++)
    {
        printf("\nCoordenada %d:",i+1);
        printf("x: %.2f\n",pontos[i].x);
        printf("y: %.2f\n",pontos[i].y);
    }
       return 0;
}