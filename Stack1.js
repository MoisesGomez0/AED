function Node(value){
    this.value = value;
    this.next = null;
}

function Stack(){
    this.first = null;
    this.push = StackPush;
    this.pop = StackPop;
    this.getFirst = StackGetFirst;
    this.getLast = StackGetLast;
    this.print = StackPrint;
}
    function StackPush(value){
        temp = this.first;
        this.first = new Node(value);
        this.first.next = temp;
        return true;
    }

    function StackPop(){
        temp = this.first;
        this.first = this.first.next;
        return temp;
    }

    function StackPrint(){
        temp = this.first;
        while(temp.next){
            console.log(temp.value);
            temp = temp.next;
        }
        console.log(temp.value);
    }

    function StackGetFirst(){
        return this.first;
    }

    function StackGetLast(){
        temp = this.first;
        while(temp.next){
            temp = temp.next;
        }
        return temp;
    }