import java.util.Scanner;

class Main_01{
    public static void main(String[] args){
        System.out.println("Hello world");
        Scanner sc = new Scanner(System.in);
        String nome;
        System.out.print("Digite seu nome: ");
        nome = sc.next();
        System.out.println("Olá " + nome);

        sc.close();
    }
}