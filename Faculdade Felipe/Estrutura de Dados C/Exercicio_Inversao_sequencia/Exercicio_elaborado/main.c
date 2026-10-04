#include <stdio.h>
#include <stdlib.h>

void inverterLista(int lista[], int tamanho) {
    int inicio = 0;
    int fim = tamanho - 1;
    while (inicio < fim) {
        int temp = lista[inicio];
        lista[inicio] = lista[fim];
        lista[fim] = temp;
        inicio++;
        fim--;
    }
}
int main() {
    int n;

    printf("Digite o numero de elementos que tera na sua sequencia:  ");
    scanf("%d", &n);

    int elementos[n];

    printf("Digite os %d numeros:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &elementos[i]);
    }

    printf("Sequencia original:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", elementos[i]);
    }
    printf("\n");

    inverterLista(elementos, n);

    printf("Sequencia invertida:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", elementos[i]);
    }
    printf("\n");

    return 0;
}
