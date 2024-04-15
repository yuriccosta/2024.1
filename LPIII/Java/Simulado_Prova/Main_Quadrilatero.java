package Simulado_Prova;

public class Main_Quadrilatero {
    public static void main(String[] args) {
        Quadrilatero a = new Quadrilatero();
        Quadrilatero b = new Quadrilatero(0, 0, -2, -1);

        System.out.println(a.eQuadrado() + " " + a.eRetangulo());
        System.out.println(b.eQuadrado() + " " + b.eRetangulo());

        System.out.println(Quadrilatero.quantosQuadrilateros() + " " + a.qualMeuNumero());
        System.out.println(Quadrilatero.quantosQuadrilateros() + " " + b.qualMeuNumero());
    }
}
