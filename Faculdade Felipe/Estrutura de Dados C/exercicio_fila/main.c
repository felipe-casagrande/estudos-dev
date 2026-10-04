#include <stdio.h>
#include <stdlib.h>

#define TAM 5

int fila[TAM];
int inicio = 0;
int fim = 0;

int filaVazia() {
    if (inicio == fim)
        return 1;
    else
        return 0;
}

int filaCheia() {
    if (fim == TAM)
        return 1;
    else
        return 0;
}

void enfileirar(int valor) {
    if (filaCheia()) {
        printf("\nFila cheia! Nao e possivel adicionar.\n");
    } else {
        fila[fim] = valor;
        fim++;
        printf("\nValor %d adicionado na fila.\n", valor);
    }
}

void desenfileirar() {
    if (filaVazia()) {
        printf("\nFila vazia! Nao ha o que remover.\n");
    } else {
        printf("\nValor %d removido da fila.\n", fila[inicio]);
        for (int i = 0; i < fim - 1; i++) {
            fila[i] = fila[i + 1];
        }
        fim--;
    }
}

void mostrarFila() {
    if (filaVazia()) {
        printf("\nFila vazia!\n");
    } else {
        printf("\nElementos da fila: ");
        for (int i = 0; i < fim; i++) {
            printf("%d ", fila[i]);
        }
        printf("\n");
    }
}

int main() {
    int opcao, valor;

    do {
        printf("\n===== MENU =====\n");
        printf("1 - Enfileirar\n");
        printf("2 - Desenfileirar\n");
        printf("3 - Mostrar fila\n");
        printf("4 - Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite um valor: ");
                scanf("%d", &valor);
                enfileirar(valor);
                break;
            case 2:
                desenfileirar();
                break;
            case 3:
                mostrarFila();
                break;
            case 4:
                printf("\nEncerrando o programa...\n");
                break;
            default:
                printf("\nOpcao invalida!\n");
        }
    } while (opcao != 4);

    return 0;
}
