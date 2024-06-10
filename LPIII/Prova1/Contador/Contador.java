package Prova1.Contador;

public class Contador {
    private int cont;
    private int max;
    private int ciclo;

    public Contador(int valorInicial, int valorMaximo){
        if (valorInicial < 0) {valorInicial = 0;}
        if (valorMaximo <= 0) {valorMaximo = 1;}
        if (valorInicial > valorMaximo){valorInicial = 0;}

        cont = valorInicial;
        max = valorMaximo;
        cont = 0;
    }

    public void incrementa(){
        cont++;
        if (cont > max){
            cont = 0;
            ciclo++;
        }
    }

    public void decrementa(){
        cont--;
        if (cont < 0){
            cont = 0;
        }
    }

    public int valorContador(){
        return cont;
    }

    public int valorCiclo(){
        return ciclo;
    }

}
