public class Carro {
    private String modelo;
    private Motor motor;

    public Carro(String modelo, int potenciaDoMotor) {
        this.modelo = modelo;
        this.motor = new Motor(potenciaDoMotor);  // Composição aqui
    }

    public void ligarCarro() {
        System.out.println("Ligando o carro modelo " + this.modelo);
        this.motor.ligar();  // Delegando a ação para o componente
    }

    public String getModel(){
        return this.modelo;
    }
}