#include <stdio.h>

struct pessoa
{
    int idade;
    float altura;
};

typedef struct pessoa Pessoa;

int main(){
    Pessoa p;
    p.idade = 5;
    p.altura = 1.65;

    printf("a idade da pessoa: %d", p.idade);
    printf("\na altura da pessoa: %.1f", p.altura);
    return 0;
}
