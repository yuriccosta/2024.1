#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct{
    char nome[100];
    char cor[100];
    char tamanho;
} camiseta;


// Função de comparação -1 se a menor ou igual que b, 1 se a maior que b, 0 se iguais
int cmpCamisas(camiseta a, camiseta b) {
    int cmp = strcmp(a.cor, b.cor);

    // Compara as cores
    if (cmp == 0){
        // Compara os tamanhos
        if (a.tamanho == b.tamanho){
            cmp = strcmp(a.nome, b.nome);
            // Compara os nomes
            if (cmp <= 0){
                return -1;
            } else{
                return 1;
            }
        } else if (a.tamanho > b.tamanho){
            return -1;
        } else {
            return 1;
        }
    } else if (cmp < 0){
        return -1;
    } else {
        return 1;
    }
}

void mostracamisa(camiseta c){
    printf("%s %c ", c.cor, c.tamanho);
    printf("%s", c.nome);
    
}



void intercala(camiseta  camisetas[], int ini, int meio, int fim){
    camiseta auxiliar[100];

    int i = ini, j = meio + 1, k = 0;

    while (i <= meio && j <= fim){
        if (cmpCamisas(camisetas[i], camisetas[j]) < 0){
            auxiliar[k++] = camisetas[i++];
        } else{
            auxiliar[k++] = camisetas[j++];
        }
    }

    while (i <= meio){
        auxiliar[k++] = camisetas[i++];
    }

    while(j <= fim){
        auxiliar[k++] = camisetas[j++];
    }

    for (i = ini, k = 0; i <= fim; i++, k++){
        camisetas[i] = auxiliar[k];
    }
}

void mergeCamisa(camiseta camisetas[], int ini, int fim){
    int meio;
    if (ini < fim){
        meio = (ini + fim) / 2;
        mergeCamisa(camisetas, ini, meio);
        mergeCamisa(camisetas, meio + 1, fim);
        intercala(camisetas, ini, meio, fim);
    }

}

int main(void){
    int N;
    scanf("%d", &N);

    camiseta camisetas[80];
    while(N > 0){
        char aux[100];
        scanf("%c", &aux[0]);
        for(int i = 0; i < N; i++){
            // Lendo a entrada
            fgets(camisetas[i].nome, 100, stdin);
            fgets(aux, 100, stdin);

            int c = 0;
            for (; aux[c] != ' '; c++){
                camisetas[i].cor[c] = aux[c];
            }
            camisetas[i].cor[c] = '\0';
            camisetas[i].tamanho = aux[c+1];
            
        }

        mergeCamisa(camisetas, 0, N-1);
       

        for (int i = 0; i < N; i++){
            mostracamisa(camisetas[i]);
        }
        printf("\n");
        scanf("%d", &N);
    }

    return 0;
}