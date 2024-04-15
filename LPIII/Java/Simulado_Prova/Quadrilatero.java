package Simulado_Prova;

// Questão 3
public class Quadrilatero {
    private double xa, ya, xb, yb, xc, yc, xd, yd;

    // Questão 4
    private static int many = 0;
    private int id;
    
    public Quadrilatero(){
        id = ++many;
        xa = yb = 0;
        xb = 0; yb = 1;
        xc = yc = 1;
        xd = 1; yd = 0;
    }

    Quadrilatero(double xa, double ya, 
    double xb, double yb, 
    double xc, double yc, 
    double xd, double yd){
        id = ++many;
        this.xa = xa;
        this.xb = xb;
        this.xc = xc;
        this.xd = xd;
        this.ya = ya;
        this.yb = yb;
        this.yc = yc;
        this.yd = yd;
    }

    Quadrilatero(double xa, double ya, double xc, double yc){
        id = ++many;
        this.xa = xa;
        this.ya = ya;
        this.xc = xc;
        this.yc = yc;

        xb = xa;
        yb = yc;

        xd = xc;
        yd = ya;
    }

    public double[] getVertices(){
        double vertices[] = {xa, ya, xb, yb, xc, yc, xd, yd};
        return vertices;
    }

    public boolean eRetangulo(){
        if (xa - xb == xc - xd){
            if(ya - yb == yd - yc){
                return true;
            }
        }

        return false;
    }

    public boolean eQuadrado(){
        if (eRetangulo()){
            if (ya - yb == xa - xd){
                return true;
            }
        }

        return false;
    }


    public static int quantosQuadrilateros(){
        return many;
    }

    public int qualMeuNumero(){
        return id;
    }
}
