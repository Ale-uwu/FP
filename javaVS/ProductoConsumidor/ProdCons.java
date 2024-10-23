package ProductoConsumidor;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ProdCons {

    static public final Lock SEMAFORO_BIN = new ReentrantLock();
    static public final int ITERACIONES = 30;
    
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
        // Prueba con 2 consumidores
        //hiloCons Consumidor2 = new hiloCons(bufferMesa);

        Productor.start();
        Consumidor.start();
        //Consumidor2.start();
        /* Anotacion sobre el segundo consumidor.
         * Para que estuviese mejor hecho el código 
         * se deberían repartir entre los consumidores
         * el numero de iteraciones porque al final van
         * a acabar haciendo bastantes mas de las necesarias
         * se podría hacer metiendo en un array a los hilos
         * y comprobando la longitud de este dentro de la ejecucion
         * de la funcion del hilo y dividiento las iteraciones
         * o yo que se algo así
         */
        try{
            Productor.join();
            Consumidor.join();
            //Consumidor2.join();
        } catch(InterruptedException e){
            e.printStackTrace();
        }
        System.out.println("*** fin de ejecucion de hilos");
    }


    public static void funcionProdcutor(QueueLimitadaImpl buffer){
        SEMAFORO_BIN.lock();
        int elemento = buffer.agregarElemento(100);
        if(elemento!=-1){
            System.out.println("+ Añadido un elemento. Elemento = "+ elemento);
            System.out.println("* Numero de elementos " + buffer.getQueue().size() );
        }
        SEMAFORO_BIN.unlock();
    }

    public static void funcionConsumidor(QueueLimitadaImpl buffer){
        SEMAFORO_BIN.lock();
        int elemento = buffer.popElemento();
        if(elemento!=-1){
            System.out.println(" - Retirado el elemento: "+ elemento);            
        }
        SEMAFORO_BIN.unlock();
    }
}
