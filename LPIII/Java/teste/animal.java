public class animal {
    private static int id = 0;
    private String tipo;

    public animal(String tipo){
        this.tipo = tipo;
        id++;
    }

    public String getTipo(){
        return tipo;
    }

    public static int getId(){
        return id;
    }

    public void fala(String fala){
        System.out.println(fala);
    }
}
