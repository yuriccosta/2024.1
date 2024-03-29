import java.util.Scanner;

public class menu {
    Scanner sc = new Scanner(System.in);

    public void printMenu(){
        System.out.println("___________Banco Popular___________");
        System.out.println("1 - Registrar Pessoa Física");
        System.out.println("2 - Checar informações da conta");
        System.out.println("3 - Depositar");
        System.out.println("4 - Sacar");
        System.out.println("5 - Transferir");
        System.out.println("6 - Aumentar limite");
        System.out.println("99 - Sair");
        System.out.print("\nDigite sua opção: ");
    }

    public pessoafisica registrar(){
        System.out.print("Digite o nome da pessoa: ");
        String nome = sc.nextLine();
        System.out.print("Digite o ID da conta: ");
        int id = sc.nextInt();
        System.out.print("Digite o saldo da conta: ");
        int saldo = sc.nextInt();
        System.out.print("Digite o limite da conta: ");
        int limite = sc.nextInt();
        System.out.println("\n");
        sc.nextLine();

        return new pessoafisica(id, nome, saldo, limite);
    }

    public pessoafisica buscaid(pessoafisica[] conta, int id){
        for (int c = 0; conta[c] != null && c < conta.length; c++){
            if (conta[c].getId() == id){
                return conta[c];
            }
        }

        System.out.println("ID: " + id  + " não encontrado\n");
        return null;
    }

    public void printconta(pessoafisica[] conta){
        System.out.print("Digite o ID da conta: ");
        int id = sc.nextInt();
        pessoafisica pessoa = buscaid(conta, id);
        if(pessoa != null){
            pessoa.printPF();
        }
        sc.nextLine();
    }

    public void depositar(pessoafisica[] conta){
        System.out.print("Digite o ID da conta: ");
        int id = sc.nextInt();
        pessoafisica pessoa = buscaid(conta, id);
        if (pessoa != null){
            System.out.print("Digite a quantia a ser depositada: ");
            int valor = sc.nextInt();
            if (pessoa.depositoPF(valor)){
                System.out.println("Deposito de " + valor + " realizado com sucesso no nome de " + pessoa.getNome());
            } else{
                System.out.println("Limite atingido");
            }
        }
        
        System.out.println("");
        sc.nextLine();
    }

    public void saque(pessoafisica[] conta){
        System.out.print("Digite o ID da conta: ");
        int id = sc.nextInt();
        pessoafisica pessoa = buscaid(conta, id);
        if (pessoa != null){
            System.out.print("Digite a quantia a ser retirada: ");
            int valor = sc.nextInt();
            if (pessoa.saquePF(valor)){
                System.out.println("Saque de " + valor + " realizado com sucesso no nome de " + pessoa.getNome());
            } else{
                System.out.println("Não foi possível realizar a transação");
            }
        }
        
        System.out.println("");
        sc.nextLine();
    }

    public void transfere(pessoafisica[] conta){
        System.out.print("Digite o ID da conta que vai enviar: ");
        int envia = sc.nextInt();
        System.out.print("Digite o ID da conta que vai receber: ");
        int recebe = sc.nextInt();
        pessoafisica origem = buscaid(conta, envia);
        pessoafisica destino = buscaid(conta, recebe);
        if (origem != null && destino != null){
            System.out.print("Digite a quantia a ser retirada: ");
            int valor = sc.nextInt();
            if (origem.transferePF(destino,valor)){
                System.out.println("Transferência no valor de " + valor + " realizado com sucesso no nome de " + origem.getNome());
                System.out.println("para " + destino.getNome());
            } else{
                System.out.println("Não há saldo suficiente");
            }
        }
        
        System.out.println("");
        sc.nextLine();
    }

}
