function Word(){
    this.random = WordRandom;
    this.alphabet = "abcdefghijklmnñopqrstuvwxyz";
}
    function WordRandom(min=2,max=8){
        letters = [];
        let r = random2int(min,max);
        for(let i = 0; i<r; i++){
            l = random2int(0,this.alphabet.length-1);
            letters.push(this.alphabet[l]);
        }
        return letters.join("");
    }