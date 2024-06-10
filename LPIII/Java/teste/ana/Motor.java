public class Motor {
    private int potencia;

    public Motor(int potencia) {
        this.potencia = potencia;
    }

    public void ligar() {
        System.out.println("Motor ligado com potência de " + this.potencia);
    }
}