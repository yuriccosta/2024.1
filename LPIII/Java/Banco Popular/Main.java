import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        menu menu = new menu();
        pessoafisica contas[] = new pessoafisica[100];
        int c = 0;
        while (true){
            menu.printMenu();
            int opt = sc.nextInt();
            if (opt == 1){
                contas[c] = menu.registrar();
                c++;
            } else if (opt == 2){
                menu.printconta(contas);
            } else if (opt == 3){
                menu.depositar(contas);
            } else if (opt == 4){
                menu.saque(contas);
            } else if (opt == 5){
                menu.transfere(contas);
            } else if (opt == 99){
                break;
            }
        }
        sc.close();
    }
}
