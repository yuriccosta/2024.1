public class ana{
    public static void main(String[] args) {
        Carro meuCarro = new Carro("Fusca", 80);
        meuCarro.ligarCarro();

        F1Car f1 = new F1Car("F1", 1000, "Aerofolio V8", "Ferrari");
        System.out.println("F1:");
        f1.ligarCarro();
    }
}

