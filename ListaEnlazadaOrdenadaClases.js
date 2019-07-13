function Node(value){
    this.value = value;
    this.next = null;
}
function LinkedList(){
    this.first = null;
    this.add = LinkedListAdd;
    this.print = LinkedListPrint;
}
    function LinkedListPrint(){
        current = this.first;
        while(current.next){
            console.log(current.value);
            current = current.next;
        }
        console.log(current.value);
    }

    function LinkedListAdd(item){
        if(!this.first){
            this.first = new Node(item);
            return true;
        }else{
            if(this.first.value <= item){
                current = this.first;
                this.first = new Node(item);
                this.first.next = current;
                return true;
            }else{
                prev = this.first;
                current = prev.next;
                while(current){
                    if(current.value <= item){
                        temp = current;
                        current = new Node(item);
                        current.next = temp;
                        prev.next = current;
                        return true;
                    }
                    prev = current;
                    current = prev.next;
                }
                current = this.first;
                while(current.next) {
                    current = current.next;
                }
                current.next = new Node(item);
                return true;
            }
        }
        return false;
    }