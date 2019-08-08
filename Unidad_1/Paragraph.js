function Paragraph(){
    this.random = ParagraphRandom;
}
    function ParagraphRandom(min = 5, max = 15){
        sentences = [];
        let r = random2int(min,max);
        sentence = new Sentence();
        for (let i = 0; i<r; i++){
            sentences.push(sentence.randomSentence());
        }
        return sentences.join(" ");

    }