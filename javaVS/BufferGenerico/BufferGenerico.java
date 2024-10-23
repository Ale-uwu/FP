package BufferGenerico;

import java.util.Queue;

public interface BufferGenerico {
    boolean addElement(Integer iElemento);
    int removeElement();
    boolean bufferLleno();
    boolean bufferVacio();
    int getElements();
    int searchPosition(int iIndice);
    void initQueue();
    void freeQueue();
    int getContadorElementos();
    Queue<Integer> getQueue();
}
