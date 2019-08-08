function Sentence(){
    this.randomSentence = SentenceRandomSentence;
    this.randomTittle = SentenceRandomTittle;
}
    function SentenceRandomSentence(min=2,max=8){
        words = [];
        let r = random2int(min,max);
        word = new Word();
        for(let i = 0; i<r; i++){
            words.push(word.random());
        }
        return `${words.join(" ")}.`
    }

    function SentenceRandomTittle(min=2,max=8){
        let words = [];
        let r = random2int(min,max);
        word = new Word();
        for(let i = 0; i<r; i++){
            words.push(word.random());
        }
        return words.join(" ")
    }