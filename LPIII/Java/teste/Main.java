public class Main {
    public static void main(String[] args) {
        animal humano = new animal("mamífero");

        animal passaro = new animal("ave");

        humano.fala("Olá");
        passaro.fala("Crá crá");

        cachorro dog = new cachorro("mamífero");
        System.out.println(dog.getTipo());
        dog.fala();
        System.out.println(animal.getId());
        System.out.println(cachorro.getId());

    }
}
