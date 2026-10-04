#include <stdio.h>
int main() {
    int vetor[] = {1, 2, 3, 4, 5, 6};
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);
    int inicio = 0, fim = tamanho - 1, temporario;
    while (inicio < fim) {
        temporario = vetor[inicio];
        vetor[inicio] = vetor[fim];
        vetor[fim] = temporario;
        inicio++;
        fim--;
    }
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
    return 0;
}
