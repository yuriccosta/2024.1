package Prova1.Elevador;

public class Elevador {
    private int cargaMaxima;
    private int cargaAtual;
    private int maxAndares;
    private int andarAtual;


    public Elevador(int cargaMaxima, int nAndares){
        if (cargaMaxima <= 0) cargaMaxima = 1;
        if (nAndares <= 0) nAndares = 1;
        
        this.cargaMaxima = cargaMaxima;
        maxAndares = nAndares;
        cargaAtual = andarAtual = 0;
    }
    
    public boolean entrar(){
        if (cargaAtual < cargaMaxima){
            cargaAtual++;
            return true;
        }
        return false;
    }

    public boolean sair(){
        if (cargaAtual > 0){
            cargaAtual--;
            return true;
        }
        return false;
    }

    public boolean sobe(){
        if (andarAtual < maxAndares){
            andarAtual++;
            return true;
        }
        return false;
    }

    public boolean desce(){
        if (andarAtual > 0){
            andarAtual++;
            return true;
        }
        return false;
    }

    public int getcargaMaxima(){
        return cargaMaxima;
    }

    public int getcargaAtual(){
        return cargaAtual;
    }

    public int getmaxAndares(){
        return maxAndares;
    }

    public int getandarAtual(){
        return andarAtual;
    }
}
