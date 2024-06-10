package Prova1.Elevador;

public class Main_Elevador {
    public static void main(String[] args) {
        Elevador torreA = new Elevador(5, 5);

        for (int c = 0; c < 10; c++){
            System.out.println("Carga atual:  " + torreA.getcargaAtual());
            System.out.println("Carga maxima: " + torreA.getcargaMaxima());
            System.out.println("Andar atual:  " + torreA.getandarAtual());
            System.out.println("Andar maximo: " + torreA.getmaxAndares() + "\n");

            if (!torreA.entrar()){
                System.err.println("Não foi possível entrar\n");
            }

            if (!torreA.sobe()){
                System.err.println("Não foi possível subir\n");
            }
        }

    }
}
