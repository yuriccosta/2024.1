public class teste{
    public static void main(String[] args) {
        System.out.print("_________________________");
        System.out.print(" Banco Popular ");
        System.out.println("_________________________\n");

        // Utilizando construtores criados
        pessoafisica ruby = new pessoafisica(1, "Ruby dos Santos", 250, 1000);
        pessoafisica joel = new pessoafisica(2, "Joel Lima", 450, 1000);

        // Antiga tentativa de registrar PF (antes de saber dos construtores)
        //ruby.regisPF(1, "Ruby dos Santos", 250);
        //joel.regisPF(2, "Joel Lima", 450);

        ruby.printPF();
        joel.printPF();

        System.out.println("Primeira Operação:");
        ruby.depositoPF(950);
        ruby.depositoPF(150);
        joel.depositoPF(350);
        ruby.printPF();
        joel.printPF();

        System.out.println("Segunda operação:");
        //joel.regisPF(10, "Ricardo Nunes", 0);
        joel.saquePF(800);
        ruby.depositoPF(500);

        ruby.printPF();
        joel.printPF();

        System.out.println("Terceira operação:");

        ruby.transferePF(joel,450);
        ruby.printPF();
        joel.printPF();
        
        // Fazendo operações para mudar limite
        System.out.println("Quarta operação:");
        ruby.depositoPF(550);
        ruby.saquePF(1000);
        ruby.depositoPF(1000);
        ruby.transferePF(joel, 500);
        System.out.println(ruby.mudalimitePF());
        ruby.printPF();
        joel.printPF();
    }
}