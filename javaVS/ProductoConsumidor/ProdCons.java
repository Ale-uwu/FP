package ProductoConsumidor;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ProdCons {

    static public final Lock SEMAFORO_BIN = new ReentrantLock();
    static public final int ITERACIONES = 20;
    
    static class hiloProd extends Thread{

        private QueueLimitadaImpl buffer;

        public hiloProd(QueueLimitadaImpl buffer){
            this.buffer = buffer;
        }

        public void run(){
            for(int i=0;i<=ITERACIONES;i++){
                funcionProdcutor(buffer);
                try{
                    Thread.sleep(2000);
                } catch(InterruptedException e){
                    e.printStackTrace();
                }
            }
        }
    }
    static class hiloCons extends Thread{

        private QueueLimitadaImpl buffer;

        public hiloCons(QueueLimitadaImpl buffer){
            this.buffer = buffer;
        }

        public void run(){
            for(int i = 0;i<ITERACIONES;i++){
                funcionConsumidor(buffer);
                try{
                    Thread.sleep(5000);
                } catch(InterruptedException e){
                    e.printStackTrace();
                }
            }
        }
    }
    public static void main(String[] args) {
        QueueLimitadaImpl bufferMesa = new QueueLimitadaImpl(8);

        hiloProd Productor = new hiloProd(bufferMesa);
        hiloCons Consumidor = new hiloCons(bufferMesa);

        Productor.start();
        Consumidor.start();

        try{
            Productor.join();
            Consumidor.join();
        } catch(InterruptedException e){
            e.printStackTrace();
        }
        System.out.println("fin de ejecucion de hilos");
    }


    public static void funcionProdcutor(QueueLimitadaImpl buffer){
        SEMAFORO_BIN.lock();
        int elemento = buffer.agregarElemento(100);
        if(elemento!=-1){
            System.out.println("Añadido un elemento. Elemento = "+ elemento);
            System.out.println("Numero de elementos " + buffer.getQueue().size() );
        }
        SEMAFORO_BIN.unlock();
    }

    public static void funcionConsumidor(QueueLimitadaImpl buffer){
        SEMAFORO_BIN.lock();
        int elemento = buffer.popElemento();
        if(elemento!=-1){
            System.out.println("Retirado el elemento: "+ elemento);            
        }
        SEMAFORO_BIN.unlock();
    }
}
