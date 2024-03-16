#include <stdio.h>
#include <string.h>

struct Atleta {
    char nome[100];
    int id, n_ouro, n_prata, n_bronze;
};

int compare_conqui(int atleta1, int atleta2, struct Atleta vatletas[]){
    int pos1 = 0, pos2 = 0;
    for (int c = 0; c < 100; c++){
        if (vatletas[c].id == atleta1){
            pos1 = c;
            break;
        }
    }

    for (int c = 0; c < 100; c++){
        if (vatletas[c].id == atleta2){
            pos2 = c;
            break;
        }
    }

    if (vatletas[pos1].n_ouro > vatletas[pos2].n_ouro){
        return atleta1;
    } else if(vatletas[pos1].n_ouro < vatletas[pos2].n_ouro){
        return atleta2;
    } else if(vatletas[pos1].n_prata > vatletas[pos2].n_prata){
        return atleta1;
    }else if(vatletas[pos1].n_prata < vatletas[pos2].n_prata){
        return atleta2;
    } else if(vatletas[pos1].n_bronze > vatletas[pos2].n_bronze){
        return atleta1;
    }else if(vatletas[pos1].n_bronze < vatletas[pos2].n_bronze){
        return atleta2;
    }else{
        return 0;
    }
}


int main(void){
    int consultanum = 0, atletanum = 0;
    struct Atleta vatletas[100];

    scanf("%d", &atletanum);
    for (int c = 0; c < atletanum; c++){
        scanf("%d %s", &vatletas[c].id , vatletas[c].nome);
        scanf("%d %d %d", &vatletas[c].n_ouro, &vatletas[c].n_prata, &vatletas[c].n_bronze);

    }

    scanf("%d", &consultanum);

    int a1, a2, resultado;
    for (int c = 0; c < consultanum; c++){
        scanf("%d %d", &a1, &a2);
        resultado = compare_conqui(a1, a2, vatletas);
        (resultado == 0) ? printf("empate\n") : printf("%d\n", resultado);
    }

    return 0;
}

