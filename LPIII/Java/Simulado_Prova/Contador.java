package Simulado_Prova;

// Questão 1
public class Contador {
    private int cont;

    public Contador(){
        cont = 0;
    }

    public Contador(int val_inicial){
        cont = val_inicial;
    }

    public void incrementa(){
        cont++;
    }

    public void incrementa(int incremento){
        cont += incremento;
    }

    public void decrementa(){
        cont--;
    }

    public int getValor(){
        return cont;
    }

    public boolean maiorQue(int val){
        if (cont > val){
            return true;
        }
        return false;
    }

    public boolean maiorOuIgualQue(int val){
        if (cont >= val){
            return true;
        }
        return false;
    }

    public boolean menorQue(int val){
        if (cont < val){
            return true;
        }
        return false;
    }

    public boolean menorOuIgualQue(int val){
        if (cont <= val){
            return true;
        }
        return false;
    }

    public boolean igual(int val){
        if (cont == val){
            return true;
        }
        return false;
    }
    
    public boolean diferente(int val){
        if (cont != val){
            return true;
        }
        return false;
    }

}
