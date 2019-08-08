function Node(value){
    this.value = value;
    this.next = null;
}
function LinkedList(){
    this.first = null;
    this.add = LinkedListAdd;//esta función se encarga de añadir un nuevo nodo al final
    this.print = LinkedListPrint;//Esta imprime el nombre de todos los nodos en orden
    this.getFirst=LinkedListGetFirst;//Duevuelve el primer nodo de la lista
    this.getLast=LinkedListGetLast;//Devuelve el último nodo de la lista
    this.addInPosition=LinkedListAddInPosition;//Esta recibe dos parámetros uno el valor de un nodo y el otro la posición donde se debe de agregar el nuevo valor
}
    function LinkedListAddInPosition(value,n){
        count = 0;
        if(n == 0){
            queue = this.first;
            this.first = new Node(value);
            this.first.next = queue; 
            return true;
        }else if(n > 0){
            current = this.first;
            before = this.first;
            while(current.next){
                current = current.next;
                count++;
                if(count == n){
                    before.next = new Node(value);
                    before.next.next=current;
                    return true;
                }
                before = before.next;
            }

        }
        return false;
    }
    function LinkedListGetFirst(){
        return this.first;
    }

    function LinkedListGetLast(){
        node = this.first;
        while(node.next){
            node = node.next;
        }
        return node;
    }

    function LinkedListAdd(value){
        if(!this.first){
            this.first = new Node(value);
        }else{
            current = this.first;
            while(current.next){
                current = current.next;
            }
            current.next = new Node(value);
        }
    }

    function LinkedListPrint(){
        current=this.first;
        while(current.next){
            console.log(current.value);
            current = current.next;
        }
        console.log(current.value);
    }
