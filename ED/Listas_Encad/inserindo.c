#include <stdio.h>
#include <stdlib.h>

typedef struct numlist{
  int num;
  struct numlist *prox;
} lista;


// Cria o elemento no inicio
lista * inicio(lista * inicio, int valor){
    lista * new = (lista*) malloc(sizeof(lista));
    new->num = valor;
    new->prox = inicio;
    return new;
}

// Cria o elemento e adiciona no final
lista * final(lista * inicio, int valor){
    lista * new = (lista*) malloc(sizeof(lista)), *aux = inicio;
    new->num = valor;
    new->prox = NULL;

    // Quando não tiver elemento na lista
    if (inicio == NULL){
        return new;
    } else {
        // Percorre a lista
        while (aux->prox != NULL){
            aux = aux->prox;
        }
        aux->prox = new;
        return inicio;
    }
}


// Percorre a lista e vai printando
void printlista(lista * inicio){
    while(inicio != NULL){
        printf("%d ", inicio->num);
        inicio = inicio->prox;
    }
    printf("\n");
}

// Percorre a lista e apaga o anterior
void limpalista(lista * inicio){
    lista * aux;
    while (inicio != NULL){
        aux = inicio->prox;
        free(inicio);
        inicio = aux;
    }
}

int main(void) {
    int n, val;
    char choice;
    scanf("%d", &n);

    while(n > 0){
        lista * encad = NULL;
        for (int c = 0; c < n; c++){
            scanf(" %c %d", &choice, &val);

            // Verifica a escolha do usuário
            if (choice == 'P'){
                encad = inicio(encad, val);
            } else{
                encad = final(encad, val);
            }
        }
        printlista(encad);
        limpalista(encad);
        scanf("%d", &n);
    }

    
    return 0;
}