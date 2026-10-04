#include <stdio.h>
#include <stdlib.h>

//Vou fazer com variaveis globais e depois mudar na funcao, pra simplificar a chamada e nao precisar criar outro parametro nas funcoes

int pilha[100];                 // Defini como 100 para pra simplificar a chamada e nao precisar criar outro parametro para as funcoes toda as vzs
int topo = -1;                  // Variavel que iremos ficar manipulando a cada insercao ou remocao de numeros.
int tamanho_maximo;             //irei definir no main





// Consideracoes: Coloquei um exit pois como perguntei ao senhor, quando tiver cheio ou vazio e eu tentar adicionar ou remover ele nao segue as proximas ordens, entao vi que podia ser feito com o exit.
// As vericacoes se esta vazia ou cheia esta dentro das funcoes


void mostrar()
{
    printf("Percorrendo pilha..\n");
    if (topo==-1){
        printf("Pilha vazia, nada a mostrar\n");
    }
    else{
        for (int i = 0; i <= topo; i++) {
        printf("%d\n", pilha[i]); // imprime: 5 10 50
    }
    }
}


void add(int valor){
    if(topo+1>=tamanho_maximo -1)                                        // Coloquei o topo +1 pq no exemplo de 1 a 10, o 10 ainda tava indo,  pq defini como -1 la em cima, agora vai dar certo
        {
            printf("Pilha ja esta cheia, encerrando programa!\n");
            printf("Veja a pilha final antes do encerramento\n");
            mostrar();
            exit(0);
        }else{
            topo++;
            pilha[topo] = valor;
            printf("Valor %d adicionado na pilha\n",valor);
        }
}



void remover(){
    if (topo==-1)
        {
            printf("Pilha esta vazia, nao tem como remover, encerrando programa!\n");
            printf("Veja a pilha final antes do encerramento.");
            mostrar();
            exit(0);
        }else{
            printf("Valor %d foi removido da pilha\n",pilha[topo]);
            topo--;
        }

}



int main(){

    // criando o tamanho da pilha
    printf("Digite o tamanho da pilha:\n");           //se digitar 10 so pode adicionar 9
    scanf("%d",&tamanho_maximo);

// chamadas de teste
    add(1);
    add(2);
    add(3);
    add(4);
    add(5);
    add(6);
    add(7);
    add(8);
    add(9);
    mostrar();
    remover();
    remover();
    remover();
    mostrar();
    remover();
    remover();
    add(11);
    mostrar();

}
