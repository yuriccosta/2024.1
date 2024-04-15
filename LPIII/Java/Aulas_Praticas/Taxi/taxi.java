package Aulas_Praticas.Taxi;


public class taxi {
    private int x, y;
    private boolean[][] mapa;

    public taxi(int x, int y, int tam){
        if (x < tam && x >= 0) {
            this.x = x;
        } else{
            this.x = 0;
        }
        if (y < tam && y >= 0){
            this.y = y;
        }else{
            this.y = 0;
        }

        mapa = new boolean[tam][tam];
    }

    public boolean up(){
        if (y != 0){
            x++;
            return true;
        } else{
            return false;
        }
    }

    public boolean down(){
        if (y < mapa.length - 1){
            y++;
            return true;
        } else{
            return false;
        }
    }

    public boolean left(){
        
    }

    public boolean right(){
        
    }

}
