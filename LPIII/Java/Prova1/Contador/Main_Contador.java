package Prova1.Contador;

public class Main_Contador {
    public static void main(String[] args) {
        Contador c = new Contador(0, 5);
        String frase = "A abelha abelhuda abelhudou as abelhas. Fala, arara loura.A arara loura falará.";

        for (int d = 0; d < frase.length(); d++){
            if (frase.charAt(d) == 'a'){
                c.incrementa();
            }
        }

        // Só para confirmar que contou certo
        System.out.println(c.valorCiclo() * 6 + c.valorContador());
    }
}
