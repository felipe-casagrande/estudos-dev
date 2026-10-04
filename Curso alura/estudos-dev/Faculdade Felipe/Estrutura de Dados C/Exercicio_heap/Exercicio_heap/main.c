#include <stdio.h>

#define MAX 100

typedef struct {
    int chave;
} Elemento;

// Função para subir (heapify-up)
void subir(Elemento T[], int i) {
    int j = i / 2;
    if (j >= 1) {
        if (T[i].chave > T[j].chave) {
            Elemento temp = T[i];
            T[i] = T[j];
            T[j] = temp;
            subir(T, j);
        }
    }
}

// Função para descer (heapify-down)
void descer(Elemento T[], int i, int n) {
    int j = 2 * i;
    while (j <= n) {
        if (j < n && T[j + 1].chave > T[j].chave) {
            j = j + 1;
        }
        if (T[i].chave < T[j].chave) {
            Elemento temp = T[i];
            T[i] = T[j];
            T[j] = temp;
            i = j;
            j = 2 * i;
        } else {
            break;
        }
    }
}

// Inserir elemento no heap (sem ponteiros)
int inserir(Elemento T[], int n, int chave) {
    n = n + 1;
    T[n].chave = chave;
    subir(T, n);
    return n; // devolve o novo tamanho
}

// Remover o maior elemento (sem ponteiros)
int remover(Elemento T[], int n) {
    if (n == 0) {
        printf("Heap vazio!\n");
        return 0;
    }

    Elemento max = T[1];
    T[1] = T[n];
    n = n - 1;
    descer(T, 1, n);

    printf("Removido: %d\n", max.chave);
    return n; // devolve o novo tamanho
}

// Mostrar heap
void mostrar(Elemento T[], int n) {
    for (int i = 1; i <= n; i++) {
        printf("%d ", T[i].chave);
    }
    printf("\n");
}

// Programa principal
int main() {
    Elemento heap[MAX];
    int n = 0;

    // Inserindo elementos
    n = inserir(heap, n, 92);
    n = inserir(heap, n, 85);
    n = inserir(heap, n, 90);
    n = inserir(heap, n, 47);
    n = inserir(heap, n, 31);
    n = inserir(heap, n, 34);
    n = inserir(heap, n, 20);
    n = inserir(heap, n, 40);
    n = inserir(heap, n, 46);
    printf("Heap atual: ");
    mostrar(heap, n);

    // Removendo elementos
    n = remover(heap, n);

    printf("Heap apos remocao: ");
    mostrar(heap, n);

    return 0;
}
