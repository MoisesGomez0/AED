function Node(value){
    this.value = value;
    this.next = null;
}

function Queue(){
    this.first = null;
    this.push = QueuePush;
    this.pop = QueuePop;
    this.print = QueuePrint;
    this.getFirst = QueueGetFirst;
    this.getLast = QueueGetLast;
}
    function QueuePush(value){
        if(!this.first){
            this.first = new Node(value);
        }else{
            current = this.first;
            while(current.next){
                current=current.next;
            }
            current.next= new Node(value);
        }
    }

    function QueuePop(){
        temp = this.first;
        this.first= this.first.next;
        return temp;
    }

    function QueuePrint(){
        temp = this.first;
        while(temp.next){
            console.log(temp.value);
            temp = temp.next;
        }
        console.log(temp.value);
    }

    function QueueGetFirst(){
        return this.first;
    }

    function QueueGetLast(){
        temp = this.first;
        while(temp.next){
            temp = temp.next;
        }
        return temp;
    }