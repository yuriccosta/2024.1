public class F1Car extends Carro{
    private String aerofoliomodel;
    private String marca;


    public F1Car(String modelo, int potenciaDoMotor, String aerofoliomodel, String marca) {
        super(modelo, potenciaDoMotor);
        this.aerofoliomodel = aerofoliomodel;
        this.marca = marca;
    }

    public void ligarCarro() {
        System.out.println("Ligando o carro modelo " + super.getModel());
        System.out.println("Aerofolio: " + this.aerofoliomodel);
        System.out.println("Marca: " + this.marca);
        super.ligarCarro();  // Delegando a ação para o componente
    }
}
