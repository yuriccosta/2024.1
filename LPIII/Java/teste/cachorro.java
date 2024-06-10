public class cachorro extends animal{
    private static int id = 0;

    public cachorro(String tipo) {
        super(tipo);
        id++;
    }

    public void fala(){
        System.out.println("Au Au");
    }

    public static int getId(){
        return id;
    }
    
}
