#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define BITS (sizeof(unsigned) * CHAR_BIT)

typedef struct No {
    unsigned chave;
    struct No *esq, *dir;
} No;

// Retorna o k-ésimo bit da chave
unsigned bit(unsigned chave, int k) {
    return (chave >> (BITS - 1 - k)) & 1;
}

// Inserção na arvore digital
No* inserir(No* p, unsigned chave, int nivel) {
    if (!p) {
        p = (No*)malloc(sizeof(No));
        if (p) {
            p->chave = chave;
            p->esq = NULL;
            p->dir = NULL;
            printf("Inserido: %u (Nivel: %d)\n", chave, nivel);
        }
        return p;
    }

    if (chave == p->chave) {
        printf("Aviso: %u ja existe.\n", chave);
        return p;
    }

    if (bit(chave, nivel) == 0)
        p->esq = inserir(p->esq, chave, nivel + 1);
    else
        p->dir = inserir(p->dir, chave, nivel + 1);

    return p;
}

// Busca na arvore digital
int buscar(No* p, unsigned x, int nivel) {
    if (!p) {
        return 0; // Nao encontrado
    }
    if (x == p->chave) {
        return 1; // Encontrado
    }
    return bit(x, nivel) == 0 ? buscar(p->esq, x, nivel + 1) : buscar(p->dir, x, nivel + 1);
}

// Impressão em ordem (simplificada)
void imprimirEmOrdem(No* p) {
    if (!p) return;
    imprimirEmOrdem(p->esq);
    printf("%u ", p->chave);
    imprimirEmOrdem(p->dir);
}

// Libera a memoria
void liberarArvore(No* p) {
    if (!p) return;
    liberarArvore(p->esq);
    liberarArvore(p->dir);
    free(p);
}

int main() {
    No* raiz = NULL;
    int op;
    unsigned v;

    do {
        printf("\n=== ARVORE DIGITAL ===\n");
        printf("1 - Inserir\n2 - Buscar\n3 - Listar todos\n4 - Sair\n");
        printf("Escolha: ");
        scanf("%d", &op);

        switch(op) {
            case 1:
                printf("Valor para inserir: ");
                scanf("%u", &v);
                raiz = inserir(raiz, v, 0);
                break;

            case 2:
                printf("Valor para buscar: ");
                scanf("%u", &v);
                if (buscar(raiz, v, 0))
                    printf("Valor %u encontrado.\n", v);
                else
                    printf("Valor %u nao encontrado.\n", v);
                break;

            case 3:
                printf("Valores na arvore: ");
                imprimirEmOrdem(raiz);
                printf("\n");
                break;

            case 4:
                printf("Saindo do programa...\n");
                liberarArvore(raiz);
                break;

            default:
                printf("Opcao invalida!\n");
        }

    } while(op != 4);

    return 0;
}