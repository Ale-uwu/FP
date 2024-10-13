package ProductoConsumidor;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class QueueLimitadaImpl implements QueueLimitada {
    
    private int tamañoMax;
    private Queue<Integer> buffer = new LinkedList<>();

    public QueueLimitadaImpl(int tamañoMax){
        this.tamañoMax = tamañoMax;
    }

    @Override
    public int agregarElemento(int e) {
        if(buffer.size()<tamañoMax){
            int elemento = generarElemento(-e, e);
            buffer.add(elemento);
            return elemento;
        } else {
            System.out.println("No se pueden añadir más elementos, el buffer está lleno");
            // Código de error
            return -1;
        }
    }

    @Override
    public Integer popElemento() {
        if(buffer.size() > 0){
            // No devería devolver nunca null 
            return buffer.poll();
        } else {
            System.out.println("No se pueden extraer elementos, el buffer está vacío");
            return -1;
        }
    }

    @Override
    public Integer getTamañoMax() {
        return this.tamañoMax;
    }

    @Override
    public boolean bufferLleno() {
        return buffer.size() == this.getTamañoMax();
    }

    @Override
    public boolean bufferVacio() {
        return buffer.size() == 0;
    }

    @Override
    public Queue<Integer> getQueue() {
        return this.buffer;
    }

    @Override
    public int generarElemento(int minimo,int maximo) {
        Random numAleatorio = new Random();
        if (minimo >= maximo) {
            throw new IllegalArgumentException("El límite inferior debe ser menor que el límite superior.");
        }
        return numAleatorio.nextInt(maximo - minimo) + minimo;
    }
}
