package Simulado_Prova;

// Questão 2
public class Main_Contador {
    public static void main(String[] args){
        Contador i = new Contador();
        Contador j = new Contador(10);

        while (i.diferente(10)){
            i.incrementa();
        }

        System.out.println("i: " + i.getValor());

        while (j.maiorOuIgualQue(0)){
            j.decrementa();
        }

        System.out.println("j: " + j.getValor());

    }
}
