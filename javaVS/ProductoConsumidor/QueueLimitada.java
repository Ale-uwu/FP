package ProductoConsumidor;

import java.util.Queue;

public interface QueueLimitada {
    /*
     * agregarElemento es en esencia igual que add/offer pero tiene en cuenta 
     * un tamaño máximo de la cola
     */
    int agregarElemento(int e);

    /*
     * Creo popElemento para que haga lo mismo que remove() o pull()
     * y no solo devuelve null o lanza excepcion sino que es personalizado
    */
    Integer popElemento();
    Integer getTamañoMax();
    boolean bufferLleno();
    boolean bufferVacio();
    Queue<Integer> getQueue();
    int generarElemento(int minimo,int maximo);
}
