#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

// -------------------------------------------------------------------------------------------------
//                                      ARVORE BINARIA DE BUSCA
// -------------------------------------------------------------------------------------------------

typedef struct no {
    int valor;
    struct no *esquerda;
    struct no *direita;
} NoBST;

NoBST* novoNoBST(int valor) {
    NoBST* no = (NoBST*) malloc(sizeof(NoBST));
    no->valor = valor;
    no->esquerda = NULL;
    no->direita = NULL;
    return no;
}

NoBST* inserirBST(NoBST* raiz, int valor) {
    if (raiz == NULL)
        return novoNoBST(valor);
    if (valor < raiz->valor)
        raiz->esquerda = inserirBST(raiz->esquerda, valor);
    else
        raiz->direita = inserirBST(raiz->direita, valor);
    return raiz;
}

void emOrdemBST(NoBST* raiz) {
    if (raiz != NULL) {
        emOrdemBST(raiz->esquerda);
        printf("%d ", raiz->valor);
        emOrdemBST(raiz->direita);
    }
}

void arvoreBinaria() {
    NoBST* raiz = NULL;

    int valores[] = {10, 3, 5, 1, 6, 9, 4, 7, 13};
    int n = sizeof(valores) / sizeof(valores[0]);

    for (int i = 0; i < n; i++)
        raiz = inserirBST(raiz, valores[i]);

    printf("\nArvore Binaria de Busca :\n");
    printf("\nElementos: 10, 3, 5, 1, 6, 9, 4, 7, 13\n");

    printf("\nPercurso em ordem: ");
    emOrdemBST(raiz);
    printf("\n");
}


// -------------------------------------------------------------------------------------------------
//                                          ARVORE AVL
// -------------------------------------------------------------------------------------------------
typedef struct NoAVL {
    int chave;
    struct NoAVL *esquerda;
    struct NoAVL *direita;
    int altura;
} NoAVL;

int alturaAVL(NoAVL *n) {
    return n ? n->altura : 0;
}

int maximo(int a, int b) {
    return (a > b) ? a : b;
}

NoAVL* novoNoAVL(int chave) {
    NoAVL* no = (NoAVL*)malloc(sizeof(NoAVL));
    if (!no) {
        fprintf(stderr, "Erro de alocacao\n");
        exit(EXIT_FAILURE);
    }
    no->chave = chave;
    no->esquerda = no->direita = NULL;
    no->altura = 1;
    return no;
}

NoAVL* rotacaoDireitaAVL(NoAVL *y) {
    NoAVL *x = y->esquerda;
    NoAVL *T2 = x->direita;
    x->direita = y;
    y->esquerda = T2;
    y->altura = maximo(alturaAVL(y->esquerda), alturaAVL(y->direita)) + 1;
    x->altura = maximo(alturaAVL(x->esquerda), alturaAVL(x->direita)) + 1;
    return x;
}

NoAVL* rotacaoEsquerdaAVL(NoAVL *x) {
    NoAVL *y = x->direita;
    NoAVL *T2 = y->esquerda;
    y->esquerda = x;
    x->direita = T2;
    x->altura = maximo(alturaAVL(x->esquerda), alturaAVL(x->direita)) + 1;
    y->altura = maximo(alturaAVL(y->esquerda), alturaAVL(y->direita)) + 1;
    return y;
}

int fatorBalanceamentoAVL(NoAVL *n) {
    if (!n) return 0;
    return alturaAVL(n->esquerda) - alturaAVL(n->direita);
}

NoAVL* inserirAVL(NoAVL* raiz, int chave) {
    if (!raiz) return novoNoAVL(chave);
    if (chave < raiz->chave)
        raiz->esquerda = inserirAVL(raiz->esquerda, chave);
    else if (chave > raiz->chave)
        raiz->direita = inserirAVL(raiz->direita, chave);
    else return raiz;

    raiz->altura = 1 + maximo(alturaAVL(raiz->esquerda), alturaAVL(raiz->direita));
    int balanceamento = fatorBalanceamentoAVL(raiz);

    if (balanceamento > 1 && chave < raiz->esquerda->chave)
        return rotacaoDireitaAVL(raiz);
    if (balanceamento < -1 && chave > raiz->direita->chave)
        return rotacaoEsquerdaAVL(raiz);
    if (balanceamento > 1 && chave > raiz->esquerda->chave) {
        raiz->esquerda = rotacaoEsquerdaAVL(raiz->esquerda);
        return rotacaoDireitaAVL(raiz);
    }
    if (balanceamento < -1 && chave < raiz->direita->chave) {
        raiz->direita = rotacaoDireitaAVL(raiz->direita);
        return rotacaoEsquerdaAVL(raiz);
    }
    return raiz;
}

void preOrdemAVL(NoAVL *raiz) {
    if (raiz) {
        printf("%d ", raiz->chave);
        preOrdemAVL(raiz->esquerda);
        preOrdemAVL(raiz->direita);
    }
}

void emOrdemAVL(NoAVL *raiz) {
    if (raiz) {
        emOrdemAVL(raiz->esquerda);
        printf("%d ", raiz->chave);
        emOrdemAVL(raiz->direita);
    }
}

void liberarArvoreAVL(NoAVL *raiz) {
    if (!raiz) return;
    liberarArvoreAVL(raiz->esquerda);
    liberarArvoreAVL(raiz->direita);
    free(raiz);
}

void arvoreAVL() {
    NoAVL *raiz = NULL;
    int valores[] = {10, 20, 30, 40, 50, 25};
    int n = sizeof(valores) / sizeof(valores[0]);

    for (int i = 0; i < n; i++)
        raiz = inserirAVL(raiz, valores[i]);

    printf("\nArvore AVL:\n");
    printf("Pre-ordem (raiz-esq-dir): ");
    preOrdemAVL(raiz);
    printf("\n");
    printf("Em ordem (ordenado): ");
    emOrdemAVL(raiz);
    printf("\n");

    liberarArvoreAVL(raiz);
}


// -------------------------------------------------------------------------------------------------
//                                      ARVORE RUBRO-NEGRA
// -------------------------------------------------------------------------------------------------
typedef enum { VERMELHO, PRETO } Cor;

typedef struct Galho {
    int valor;
    Cor cor;
    struct Galho *esq, *dir, *pai;
} Galho;

Galho* criaGalho(int valor) {
    Galho* galho = (Galho*) malloc(sizeof(Galho));
    galho->valor = valor;
    galho->cor = VERMELHO;
    galho->esq = galho->dir = galho->pai = NULL;
    return galho;
}

Galho* rodaEsquerda(Galho* raiz, Galho* x) {
    Galho* y = x->dir;
    x->dir = y->esq;
    if (y->esq) y->esq->pai = x;
    y->pai = x->pai;
    if (!x->pai) raiz = y;
    else if (x == x->pai->esq) x->pai->esq = y;
    else x->pai->dir = y;
    y->esq = x;
    x->pai = y;
    return raiz;
}

Galho* rodaDireita(Galho* raiz, Galho* y) {
    Galho* x = y->esq;
    y->esq = x->dir;
    if (x->dir) x->dir->pai = y;
    x->pai = y->pai;
    if (!y->pai) raiz = x;
    else if (y == y->pai->esq) y->pai->esq = x;
    else y->pai->dir = x;
    x->dir = y;
    y->pai = x;
    return raiz;
}

Galho* arrumaInsercao(Galho* raiz, Galho* z) {
    while (z->pai && z->pai->cor == VERMELHO) {
        Galho* avo = z->pai->pai;
        if (z->pai == avo->esq) {
            Galho* tio = avo->dir;
            if (tio && tio->cor == VERMELHO) {
                z->pai->cor = PRETO;
                tio->cor = PRETO;
                avo->cor = VERMELHO;
                z = avo;
            } else {
                if (z == z->pai->dir) {
                    z = z->pai;
                    raiz = rodaEsquerda(raiz, z);
                }
                z->pai->cor = PRETO;
                avo->cor = VERMELHO;
                raiz = rodaDireita(raiz, avo);
            }
        } else {
            Galho* tio = avo->esq;
            if (tio && tio->cor == VERMELHO) {
                z->pai->cor = PRETO;
                tio->cor = PRETO;
                avo->cor = VERMELHO;
                z = avo;
            } else {
                if (z == z->pai->esq) {
                    z = z->pai;
                    raiz = rodaDireita(raiz, z);
                }
                z->pai->cor = PRETO;
                avo->cor = VERMELHO;
                raiz = rodaEsquerda(raiz, avo);
            }
        }
    }
    raiz->cor = PRETO;
    return raiz;
}

Galho* insereVP(Galho* raiz, int valor) {
    Galho* novoGalho = criaGalho(valor);
    Galho* ultimoVisitado = NULL;
    Galho* atual = raiz;

    while (atual) {
        ultimoVisitado = atual;
        if (novoGalho->valor < atual->valor) atual = atual->esq;
        else atual = atual->dir;
    }

    novoGalho->pai = ultimoVisitado;
    if (!ultimoVisitado) raiz = novoGalho;
    else if (novoGalho->valor < ultimoVisitado->valor) ultimoVisitado->esq = novoGalho;
    else ultimoVisitado->dir = novoGalho;

    return arrumaInsercao(raiz, novoGalho);
}

Galho* pegaMin(Galho* x) {
    while (x->esq) x = x->esq;
    return x;
}

Galho* arrumaRemocao(Galho* raiz, Galho* x, Galho* paiDeX) {
    while (x != raiz && (!x || x->cor == PRETO)) {
        if (x == paiDeX->esq) {
            Galho* irmao = paiDeX->dir;
            if (irmao->cor == VERMELHO) {
                irmao->cor = PRETO;
                paiDeX->cor = VERMELHO;
                raiz = rodaEsquerda(raiz, paiDeX);
                irmao = paiDeX->dir;
            }
            if ((!irmao->esq || irmao->esq->cor == PRETO) &&
                (!irmao->dir || irmao->dir->cor == PRETO)) {
                irmao->cor = VERMELHO;
                x = paiDeX;
                paiDeX = x->pai;
            } else {
                if (!irmao->dir || irmao->dir->cor == PRETO) {
                    if(irmao->esq) irmao->esq->cor = PRETO;
                    irmao->cor = VERMELHO;
                    raiz = rodaDireita(raiz, irmao);
                    irmao = paiDeX->dir;
                }
                irmao->cor = paiDeX->cor;
                paiDeX->cor = PRETO;
                if(irmao->dir) irmao->dir->cor = PRETO;
                raiz = rodaEsquerda(raiz, paiDeX);
                x = raiz;
            }
        } else {
            Galho* irmao = paiDeX->esq;
            if (irmao->cor == VERMELHO) {
                irmao->cor = PRETO;
                paiDeX->cor = VERMELHO;
                raiz = rodaDireita(raiz, paiDeX);
                irmao = paiDeX->esq;
            }
            if ((!irmao->esq || irmao->esq->cor == PRETO) &&
                (!irmao->dir || irmao->dir->cor == PRETO)) {
                irmao->cor = VERMELHO;
                x = paiDeX;
                paiDeX = x->pai;
            } else {
                if (!irmao->esq || irmao->esq->cor == PRETO) {
                    if(irmao->dir) irmao->dir->cor = PRETO;
                    irmao->cor = VERMELHO;
                    raiz = rodaEsquerda(raiz, irmao);
                    irmao = paiDeX->esq;
                }
                irmao->cor = paiDeX->cor;
                paiDeX->cor = PRETO;
                if(irmao->esq) irmao->esq->cor = PRETO;
                raiz = rodaDireita(raiz, paiDeX);
                x = raiz;
            }
        }
    }
    if(x) x->cor = PRETO;
    return raiz;
}

Galho* removeGalho(Galho* raiz, int chave) {
    Galho* aRemover = raiz;
    while(aRemover && aRemover->valor != chave) {
        if(chave < aRemover->valor) aRemover = aRemover->esq;
        else aRemover = aRemover->dir;
    }
    if(!aRemover) return raiz;

    Galho* praSubstituir = aRemover;
    Cor corOriginal = praSubstituir->cor;
    Galho* x = NULL;
    Galho* paiDeX = NULL;

    if(!aRemover->esq) {
        x = aRemover->dir;
        paiDeX = aRemover->pai;
        if(aRemover->pai) {
            if(aRemover->pai->esq == aRemover) aRemover->pai->esq = aRemover->dir;
            else aRemover->pai->dir = aRemover->dir;
        } else raiz = aRemover->dir;
        if(aRemover->dir) aRemover->dir->pai = aRemover->pai;
    } else if(!aRemover->dir) {
        x = aRemover->esq;
        paiDeX = aRemover->pai;
        if(aRemover->pai) {
            if(aRemover->pai->esq == aRemover) aRemover->pai->esq = aRemover->esq;
            else aRemover->pai->dir = aRemover->esq;
        } else raiz = aRemover->esq;
        if(aRemover->esq) aRemover->esq->pai = aRemover->pai;
    } else {
        praSubstituir = pegaMin(aRemover->dir);
        corOriginal = praSubstituir->cor;
        x = praSubstituir->dir;
        if(praSubstituir->pai == aRemover) paiDeX = praSubstituir;
        else {
            if(praSubstituir->pai) {
                if(praSubstituir->pai->esq == praSubstituir) praSubstituir->pai->esq = praSubstituir->dir;
                else praSubstituir->pai->dir = praSubstituir->dir;
            }
            if(praSubstituir->dir) praSubstituir->dir->pai = praSubstituir->pai;
            praSubstituir->dir = aRemover->dir;
            if(praSubstituir->dir) praSubstituir->dir->pai = praSubstituir;
            paiDeX = praSubstituir->pai;
        }
        if(aRemover->pai) {
            if(aRemover->pai->esq == aRemover) aRemover->pai->esq = praSubstituir;
            else aRemover->pai->dir = praSubstituir;
        } else raiz = praSubstituir;
        praSubstituir->pai = aRemover->pai;
        praSubstituir->esq = aRemover->esq;
        if(praSubstituir->esq) praSubstituir->esq->pai = praSubstituir;
        praSubstituir->cor = aRemover->cor;
    }
    free(aRemover);
    if(corOriginal == PRETO)
        raiz = arrumaRemocao(raiz, x, paiDeX);
    return raiz;
}

// função para printar a árvore em linha (percurso em-ordem)
void emOrdemRubroNegra(Galho* galho) {
    if (galho) {
        emOrdemRubroNegra(galho->esq);
        printf("%d(%c) ", galho->valor, galho->cor == VERMELHO ? 'V' : 'P');
        emOrdemRubroNegra(galho->dir);
    }
}

void arvoreRubroNegra() {
    Galho* raiz = NULL;
    int valores[] = {20,15,10,18,5,12,17,21};
    int n = sizeof(valores)/sizeof(valores[0]);

    printf("\nArvore Rubro-Negra:\n");
    for(int i=0;i<n;i++) {
        raiz = insereVP(raiz, valores[i]);
    }
    printf("Arvore apos insercoes (em ordem): ");
    emOrdemRubroNegra(raiz);
    printf("\n");

    printf("\nRemovendo 15 e 20...\n");
    raiz = removeGalho(raiz, 15);
    raiz = removeGalho(raiz, 20);

    printf("Arvore apos remocoes (em ordem): ");
    emOrdemRubroNegra(raiz);
    printf("\n");
}

// -------------------------------------------------------------------------------------------------
//                                      ARVORE DIGITAL (TRIE)
// -------------------------------------------------------------------------------------------------
#define BITS (sizeof(unsigned) * CHAR_BIT)

typedef struct NodeTrie {
    unsigned chave;
    struct NodeTrie *esq, *dir;
} NodeTrie;

// Retorna o k-ésimo bit da chave
unsigned bit(unsigned chave, int k) {
    return (chave >> (BITS - 1 - k)) & 1;
}

// Inserção na arvore digital
NodeTrie* inserirTrie(NodeTrie* p, unsigned chave, int nivel) {
    if (!p) {
        p = (NodeTrie*)malloc(sizeof(NodeTrie));
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
        p->esq = inserirTrie(p->esq, chave, nivel + 1);
    else
        p->dir = inserirTrie(p->dir, chave, nivel + 1);

    return p;
}

// Busca na arvore digital
int buscarTrie(NodeTrie* p, unsigned x, int nivel) {
    if (!p) {
        return 0; // Nao encontrado
    }
    if (x == p->chave) {
        return 1; // Encontrado
    }
    return bit(x, nivel) == 0 ? buscarTrie(p->esq, x, nivel + 1) : buscarTrie(p->dir, x, nivel + 1);
}

// Impressão em ordem (simplificada)
void imprimirEmOrdemTrie(NodeTrie* p) {
    if (!p) return;
    imprimirEmOrdemTrie(p->esq);
    printf("%u ", p->chave);
    imprimirEmOrdemTrie(p->dir);
}

// Libera a memoria
void liberarArvoreTrie(NodeTrie* p) {
    if (!p) return;
    liberarArvoreTrie(p->esq);
    liberarArvoreTrie(p->dir);
    free(p);
}

void arvoreDigital() {
    NodeTrie* raiz = NULL;
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
                raiz = inserirTrie(raiz, v, 0);
                break;

            case 2:
                printf("Valor para buscar: ");
                scanf("%u", &v);
                if (buscarTrie(raiz, v, 0))
                    printf("Valor %u encontrado.\n", v);
                else
                    printf("Valor %u nao encontrado.\n", v);
                break;

            case 3:
                printf("Valores na arvore: ");
                imprimirEmOrdemTrie(raiz);
                printf("\n");
                break;

            case 4:
                printf("Saindo da Arvore Digital...\n");
                liberarArvoreTrie(raiz);
                break;

            default:
                printf("Opcao invalida!\n");
        }
    } while(op != 4);
}

// -------------------------------------------------------------------------------------------------
//                                      ARVORE DE HUFFMAN
// -------------------------------------------------------------------------------------------------
typedef struct NodeHuff {
    char ch;
    int freq;
    struct NodeHuff *left, *right;
} NodeHuff;

NodeHuff* createNodeHuff(char ch, int freq, NodeHuff* left, NodeHuff* right) {
    NodeHuff* node = (NodeHuff*) malloc(sizeof(NodeHuff));
    node->ch = ch;
    node->freq = freq;
    node->left = left;
    node->right = right;
    return node;
}

int cmp(const void* a, const void* b) {
    NodeHuff* n1 = *(NodeHuff**)a;
    NodeHuff* n2 = *(NodeHuff**)b;
    return n1->freq - n2->freq;
}

NodeHuff* buildHuffmanTree(char chars[], int freq[], int size) {
    NodeHuff* nodes[256];
    for (int i = 0; i < size; i++) {
        nodes[i] = createNodeHuff(chars[i], freq[i], NULL, NULL);
    }
    int n = size;

    while (n > 1) {
        qsort(nodes, n, sizeof(NodeHuff*), cmp);

        NodeHuff* left = nodes[0];
        NodeHuff* right = nodes[1];

        NodeHuff* parent = createNodeHuff('$', left->freq + right->freq, left, right);

        nodes[0] = parent;
        nodes[1] = nodes[n-1];
        n--;
    }
    return nodes[0];
}

void printCodes(NodeHuff* root, char code[], int depth) {
    if (!root) return;
    if (!root->left && !root->right) {
        code[depth] = '\0';
        printf("%c: %s\n", root->ch, code);
        return;
    }
    code[depth] = '0';
    printCodes(root->left, code, depth+1);
    code[depth] = '1';
    printCodes(root->right, code, depth+1);
}

void arvoreHuffman() {
    char text[] = "bananaaa";
    int freq[256] = {0};

    for (int i = 0; text[i]; i++)
        freq[(unsigned char)text[i]]++;

    char chars[256];
    int f[256];
    int size = 0;

    for (int i = 0; i < 256; i++) {
        if (freq[i] > 0) {
            chars[size] = i;
            f[size] = freq[i];
            size++;
        }
    }

    NodeHuff* root = buildHuffmanTree(chars, f, size);

    printf("\nArvore de Huffman:\n");
    printf("Tabela de Huffman:\n");
    char code[100];
    printCodes(root, code, 0);
}

// -------------------------------------------------------------------------------------------------
//                                              ARVORE B
// -------------------------------------------------------------------------------------------------
#define ORDEM 2
#define MAX_CHAVES (2*ORDEM-1)
#define MAX_FILHOS (2*ORDEM)

typedef struct NoB {
    int n;
    int chaves[MAX_CHAVES];
    struct NoB* filhos[MAX_FILHOS];
    int folha;
} NoB;

NoB* criaNoB(int folha) {
    NoB* no = (NoB*) malloc(sizeof(NoB));
    no->n = 0;
    no->folha = folha;
    for (int i = 0; i < MAX_FILHOS; i++)
        no->filhos[i] = NULL;
    return no;
}

void divideFilho(NoB* pai, int i, NoB* cheio) {
    NoB* novo = criaNoB(cheio->folha);
    novo->n = ORDEM - 1;

    for (int j = 0; j < ORDEM-1; j++)
        novo->chaves[j] = cheio->chaves[j+ORDEM];

    if (!cheio->folha) {
        for (int j = 0; j < ORDEM; j++)
            novo->filhos[j] = cheio->filhos[j+ORDEM];
    }

    cheio->n = ORDEM - 1;

    for (int j = pai->n; j >= i+1; j--)
        pai->filhos[j+1] = pai->filhos[j];
    pai->filhos[i+1] = novo;

    for (int j = pai->n-1; j >= i; j--)
        pai->chaves[j+1] = pai->chaves[j];

    pai->chaves[i] = cheio->chaves[ORDEM-1];
    pai->n++;
}

void insereNaoCheio(NoB* no, int k) {
    int i = no->n - 1;

    if (no->folha) {
        while (i >= 0 && k < no->chaves[i]) {
            no->chaves[i+1] = no->chaves[i];
            i--;
        }
        no->chaves[i+1] = k;
        no->n++;
    } else {
        while (i >= 0 && k < no->chaves[i]) i--;
        i++;
        if (no->filhos[i]->n == MAX_CHAVES) {
            divideFilho(no, i, no->filhos[i]);
            if (k > no->chaves[i]) i++;
        }
        insereNaoCheio(no->filhos[i], k);
    }
}

NoB* insereB(NoB* raiz, int k) {
    if (raiz == NULL) {
        raiz = criaNoB(1);
        raiz->chaves[0] = k;
        raiz->n = 1;
        return raiz;
    }

    if (raiz->n == MAX_CHAVES) {
        NoB* novaRaiz = criaNoB(0);
        novaRaiz->filhos[0] = raiz;
        divideFilho(novaRaiz, 0, raiz);

        int i = 0;
        if (k > novaRaiz->chaves[0]) i++;
        insereNaoCheio(novaRaiz->filhos[i], k);

        return novaRaiz;
    } else {
        insereNaoCheio(raiz, k);
        return raiz;
    }
}

void imprimeArvoreB(NoB* raiz, int nivel) {
    if (raiz == NULL) return;
    for (int i = 0; i < nivel; i++) printf("    ");
    printf("[");
    for (int i = 0; i < raiz->n; i++) {
        printf("%d", raiz->chaves[i]);
        if (i < raiz->n - 1) printf(" ");
    }
    printf("]\n");
    if (!raiz->folha) {
        for (int i = 0; i <= raiz->n; i++) {
            imprimeArvoreB(raiz->filhos[i], nivel+1);
        }
    }
}

void arvoreB() {
    NoB* raiz = NULL;
    int valores[] = {10, 20, 5, 6, 12, 30, 7, 17};
    int n = sizeof(valores)/sizeof(valores[0]);

    for (int i = 0; i < n; i++)
        raiz = insereB(raiz, valores[i]);

    printf("\nArvore B:\n");
    imprimeArvoreB(raiz, 0);
}

// -------------------------------------------------------------------------------------------------
//                                         ARVORE BALANCEADA
// -------------------------------------------------------------------------------------------------

typedef struct No {
    int valor;
    short altura;
    struct No *esq, *dir;
} No;

short alturaNo(No *no) {
    return (no) ? no->altura : -1;
}

short maior(short a, short b) {
    return (a > b) ? a : b;
}

short balanceamento(No *no) {
    if (no == NULL) {
        return 0;
    }
    return alturaNo(no->esq) - alturaNo(no->dir);
}

No* novNo(int x) {
    No* novo = (No*)malloc(sizeof(No));
    if (novo) {
        novo->valor = x;
        novo->esq = novo->dir = NULL;
        novo->altura = 0;
    }
    return novo;
}

No* rotacaoEsquerdaNova(No* x) {
    No* y = x->dir;
    No* T2 = y->esq;

    y->esq = x;
    x->dir = T2;

    x->altura = maior(alturaNo(x->esq), alturaNo(x->dir)) + 1;
    y->altura = maior(alturaNo(y->esq), alturaNo(y->dir)) + 1;

    return y;
}

No* rotacaoDireitaNova(No* y) {
    No* x = y->esq;
    No* T2 = x->dir;

    x->dir = y;
    y->esq = T2;

    y->altura = maior(alturaNo(y->esq), alturaNo(y->dir)) + 1;
    x->altura = maior(alturaNo(x->esq), alturaNo(x->dir)) + 1;

    return x;
}

No* inserirBalanceado(No* no, int valor) {
    if (no == NULL) {
        return novNo(valor);
    }
    if (valor < no->valor) {
        no->esq = inserirBalanceado(no->esq, valor);
    } else if (valor > no->valor) {
        no->dir = inserirBalanceado(no->dir, valor);
    } else {
        return no;
    }

    no->altura = 1 + maior(alturaNo(no->esq), alturaNo(no->dir));
    int balanco = balanceamento(no);

    if (balanco > 1 && valor < no->esq->valor)
        return rotacaoDireitaNova(no);

    if (balanco < -1 && valor > no->dir->valor)
        return rotacaoEsquerdaNova(no);

    if (balanco > 1 && valor > no->esq->valor) {
        no->esq = rotacaoEsquerdaNova(no->esq);
        return rotacaoDireitaNova(no);
    }

    if (balanco < -1 && valor < no->dir->valor) {
        no->dir = rotacaoDireitaNova(no->dir);
        return rotacaoEsquerdaNova(no);
    }

    return no;
}

void imprimirEmOrdem(No* no) {
    if (no == NULL) {
        return;
    }
    imprimirEmOrdem(no->esq);
    printf("%d ", no->valor);
    imprimirEmOrdem(no->dir);
}

void liberarArvore(No* no) {
    if (no == NULL) {
        return;
    }
    liberarArvore(no->esq);
    liberarArvore(no->dir);
    free(no);
}

void arvoreBalanceada() {
    No *raiz = NULL;
    int valores[] = {10, 5, 15, 3, 7, 18};
    int n = sizeof(valores) / sizeof(valores[0]);

    printf("\nArvore Balanceada :\n");
    for (int i = 0; i < n; i++) {
        raiz = inserirBalanceado(raiz, valores[i]);
    }

    printf("Valores na arvore (em ordem): ");
    imprimirEmOrdem(raiz);
    printf("\n");

    liberarArvore(raiz);
}


// -------------------------------------------------------------------------------------------------
//                                      MENU PRINCIPAL
// -------------------------------------------------------------------------------------------------
int main() {
    int opcao;

    do {
        printf("\n--- MENU DE ARVORES ---\n");
        printf("1. Arvore Binaria de Busca\n");
        printf("2. Arvore AVL\n");
        printf("3. Arvore Rubro-Negra\n");
        printf("4. Arvore Digital (Trie)\n");
        printf("5. Arvore de Huffman\n");
        printf("6. Arvore B\n");
        printf("7. Arvore Balanceada \n");
        printf("8. Sair\n");
        printf("Escolha uma opcao: ");

        while (scanf("%d", &opcao) != 1 || opcao < 1 || opcao > 8) {
            printf("Opcao invalida. Tente novamente: ");
            while(getchar() != '\n');
        }

        switch(opcao) {
            case 1:
                arvoreBinaria();
                break;
            case 2:
                arvoreAVL();
                break;
            case 3:
                arvoreRubroNegra();
                break;
            case 4:
                arvoreDigital();
                break;
            case 5:
                arvoreHuffman();
                break;
            case 6:
                arvoreB();
                break;
            case 7:
                arvoreBalanceada();
                break;
            case 8:
                printf("Saindo...\n");
                break;
        }
    } while (opcao != 8);

    return 0;
}
