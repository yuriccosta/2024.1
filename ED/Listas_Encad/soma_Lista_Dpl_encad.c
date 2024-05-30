#include <stdio.h>
#include <stdlib.h>

typedef struct Listadpl{
    int num;
    struct Listadpl *ant;
    struct Listadpl *prox;
} duplaEncad;


// Cria um novo nó e adiciona no final da lista
duplaEncad * addfinal(duplaEncad * inicio){
    duplaEncad *new = malloc(sizeof(duplaEncad)), *aux = inicio;
    new->prox = NULL;

    scanf("%d", &new->num);

    if (inicio == NULL){
        new->ant = NULL;
        return new;
    }

    
    // Percorre até chegar no último elemento
    while (aux->prox != NULL){
        aux = aux->prox;
    }

    aux->prox = new;
    new->ant = aux;
    return inicio;
}

int main(void){
    
    int N;
    //while(scanf("%d", &N)){
    while(1){
        scanf("%d", &N);
        if(N <= 0) break;

        duplaEncad *lista1 = NULL, *lista2 = NULL;

        // Cria a lista 1
        for (int c = 0; c < N; c++){
            lista1 = addfinal(lista1);
        }
        
        // Cria a lista 2
        for (int c = 0; c < N; c++){
            lista2 = addfinal(lista2);
        }

        // Percorre a lista 2 até o final para que possamos fazer a soma ao contrário        
        duplaEncad *final = lista2;
        while (final-> prox != NULL){
            final = final->prox;
        }

        // Vai printando os valores e limpando a lista
        duplaEncad *aux;
        while(lista1 != NULL){
            printf("%d ", lista1->num + final->num);

            // Limpa lista1
            aux = lista1;
            lista1 = lista1->prox;
            free(aux);

            aux = final;
            final = final->ant;
            free(aux);
        }
        printf("\n");

    }

    return 0;
}
