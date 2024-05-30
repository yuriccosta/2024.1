#include <stdio.h>
#include <stdlib.h>

typedef struct ListaCir{
    int N;
    struct ListaCir *prox;
} cirEncad;


// Cria a lista circular ja com as numerações dos jogadores
cirEncad * criaLista(cirEncad * inicio, int N){
    inicio = malloc(sizeof(cirEncad));
    inicio->N = 1;
    inicio->prox = inicio;

    cirEncad * aux = inicio, *new;
    for (int c = 2; c <= N; c++){
        new = malloc(sizeof(cirEncad));
        new->N = c;
        new->prox = inicio;

        aux->prox = new;
        aux = new;
    }

    return inicio;
}

// Elimina os jogadores com base no K até restar 1. Limpa toda a memória alocada até o final do programa
int elimina(cirEncad * inicio, int K){
    cirEncad *aux = inicio, *ant = inicio;
    while (1){
        // Percorre a lista e faz aux ser o elemento que queremos eliminar e ant ser o anterior a ele
        for (int c = 1; c < K; c++){
            ant = aux;
            aux = aux->prox;
        }

        // Verifica se aux é igual ao anterior para depois dividir nos dois casos
        if (aux == ant){
            // Verifica se estamos no caso 1: com apenas um elemento na lista
            if (aux->prox == aux){
                int N = aux->N;
                free(aux);
                
                // Retorna o valor e encerra a função
                return N;
            }
            
            //Caso 2: Percorre até o final da lista para poder apontar o final com o novo inicio
            while (ant->prox != aux){
                ant = ant->prox;
            }

            // Linka o final com o novo inicio e elimina o elemento atual
            aux = aux->prox;
            free(ant->prox);
            ant->prox = aux;
        } else{
            // Elimina o elemento atual e linka o anterior com o proximo
            ant->prox = aux->prox;
            free(aux);
            aux = ant->prox;
        }
    }
}

int main(void){
    
    int nteste;
    scanf("%d", &nteste);

    int N, K;
    cirEncad *roda;
    for (int c = 0; c < nteste; c++){
        scanf("%d %d", &N, &K);
        roda = criaLista(roda, N);
        printf("%d\n", elimina(roda, K));
    }


    return 0;
}
