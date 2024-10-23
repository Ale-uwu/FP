package BufferGenerico;
import java.util.LinkedList;
import java.util.Queue;


public class BufferGenericoImpl implements BufferGenerico {
        final int TAMAÑO_BUFFER = 8;
        private int iContadorElementos;
        // No hacen falta ya que Queue tiene los metodos add y remove
        /*private int iIndiceAgregarElemento;
        private int iIndiceQuitarElemento;*/
        private Queue<Integer> buffer = new LinkedList<>();
        public boolean addElement(Integer iElemento){
                boolean iValidarAñadirElemento = false;
                if(!bufferLleno()){
                        buffer.add(iElemento);
                        iValidarAñadirElemento = true;
                }
                return iValidarAñadirElemento;
                
        }
        public int removeElement(){
                int iElemento = -1;
                if(!bufferVacio()){
                        iElemento = buffer.remove(); 
                }
                return iElemento;
        }
        public boolean bufferLleno(){
                return buffer.size() == TAMAÑO_BUFFER;             
        }
        public boolean bufferVacio() {
                return buffer.size() == 0;
        }
        public int getElements() {
                return buffer.size();
        }
        public int searchPosition(int iIndice) {
                int iElemento = -1;
                int iContador = 0;
                if(!bufferVacio()){
                        for(int iElementoBuffer : buffer){
                                if(iContador == iIndice && iContador<=TAMAÑO_BUFFER){
                                        iElemento = iElementoBuffer;
                                }
                                iContador++;
                        }
                }
                return iElemento;
        }
        public void initQueue() {
                this.iContadorElementos = 0;
        }
        public void freeQueue() {
                
        }
        public int getContadorElementos(){
                return this.iContadorElementos;
        }
        public Queue<Integer> getQueue(){
                return this.buffer;
        }
        
}
