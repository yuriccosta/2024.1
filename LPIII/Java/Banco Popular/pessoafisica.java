public class pessoafisica {
    private int id;
    private String nome;
    private int saldo;
    private int limite;
    private int pontos;

    public pessoafisica (int id, String nome, int saldo, int limite){
        this.id = id;
        this.nome = nome;
        this.limite = limite;
        pontos = saldo / 70;

        if (saldo > limite){
            this.saldo = limite;
        } else{
            this.saldo = saldo;
        }

    }

    public void printPF (){
        System.out.println("\nNome: " + nome);
        System.out.println("ID: " + id);
        System.out.println("Saldo: " + saldo);
        System.out.println("Limite: " + limite);
        System.out.println("Pontos: " + pontos + "\n");
    }

    public boolean depositoPF (int valor){
        if (valor + saldo > limite){
            return false;
        } else{
            saldo += valor;
            pontos += valor / 100;
            return true;
        }
    }

    public boolean saquePF (int valor){
        if (saldo - valor < 0){
            return false;
        } else{
            saldo -= valor;
            pontos += valor / 150;
            return true;
        }
    }

    public boolean transferePF(pessoafisica recebe, int valor){
        if (recebe.saldo + valor < recebe.limite){
            if (this.saquePF(valor)){
                pontos += valor / 70;
                return recebe.depositoPF(valor);
            }
        }
        
        return false;
    }

    public boolean mudalimitePF(){
        if (pontos >= limite * 0.03){
            limite += (limite * 0.15) + (pontos * 2);
            pontos = 0;
            return true;
        } else{
            return false;
        }
    }

    public int getId(){
        return id;
    }

    public String getNome(){
        return nome;
    }

}
