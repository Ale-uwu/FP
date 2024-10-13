class ejecucionHilo extends Thread{
    public void run(){
        for(int i = 0;i<5;i++){
            System.out.println("Hilo en ejecución: " + i);
            try{
                Thread.sleep(1000);
            } catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}

public class E1_hiloJ{
    public static void main(String[] args) {
        ejecucionHilo hilo1 = new ejecucionHilo();
        hilo1.start();

        // Código que se ejecuta paralelo al hilo
        // Lo que sería el Hilo principal vaya
        try {
            for(int i = 0;i<7;i++){
                System.out.println("Eyeyey n: " + i);
                Thread.sleep(1000);
            }
            hilo1.join();  // Espera a que hilo1 termine
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Código que se ejecuta luego de que acabe el hilo (después del join)
        System.out.println("mimimimimi");
    }
}