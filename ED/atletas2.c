#include <stdio.h>
#include <stdlib.h>

typedef struct Atleta {
    char nome[100];
    int id, n_ouro, n_prata, n_bronze;
    struct Atleta *prox;
} atleta;



atleta * insereAtleta(atleta * inicio){
    atleta * new = (atleta*) malloc(sizeof(atleta)), *aux = inicio;
    scanf("%d %s", &new->id, new->nome);
    scanf("%d %d %d", &new->n_ouro, &new->n_prata, &new->n_bronze);
    new->prox = NULL;

    // Caso seja o primeiro elemento
    if (inicio == NULL){
        return new;
    } else{
        //Percorre até chegar no último elemento, para adicionar no final
        while(aux->prox != NULL){
            aux = aux->prox;
        }
        aux->prox = new;
        return inicio;
    }
}

atleta * removepares (atleta * inicio){
    int mtotal;
    atleta * aux = inicio, *ant = inicio;

    // Caso a lista só tenha um elemento
    if (aux->prox == NULL){
        mtotal = aux->n_ouro + aux->n_prata + aux->n_bronze;
        if (mtotal % 2 == 0){
            free(aux);
            return NULL;
        }
    }

    // Percorre a lista
    while (aux->prox != NULL){
        // Recebe o total de medalhas
        mtotal = aux->n_ouro + aux->n_prata + aux->n_bronze;
        
        // Verifica se o total de medalhas é par
        if (mtotal % 2 == 0){
            // Se quem está percorrendo for igual ao início não temos anterior
            if (aux == inicio){
                inicio = inicio->prox;
                free(aux);
                aux = inicio;
                // Voltamos pro começo do loop para não alterar o valor de aux
                continue;
            } else{
                // O próximo do anterior é igual ao próximo do atual
                ant->prox = aux->prox;
                free(aux);
                aux = ant;
            }
        }
        // Faz com que var fique sempre antes de quem está percorrendo
        ant = aux;
        aux = aux->prox;
    }

    // Verifica o último elemento da lista
    mtotal = aux->n_ouro + aux->n_prata + aux->n_bronze;
    if (mtotal % 2 == 0){
        ant->prox = NULL;
        free(aux);
    }

    return inicio;
}

// Função de printar a lista
void printlista(atleta * inicio){
    while(inicio != NULL){
        printf("%d ", inicio->id);
        inicio = inicio->prox;
    }
    printf("\n");
}

int main (void){
    int n;
    scanf("%d", &n);

    atleta * encad = NULL;

    //Insere os atletas
    for (int c = 0; c < n; c++){
        encad = insereAtleta(encad);
    }

    // Remove os pares
    encad = removepares(encad);
    printlista(encad);
    

    return 0;
}



