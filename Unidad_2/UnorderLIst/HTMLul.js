function HTMLul(){
    this.convert = HTMLulConvert
}
    function HTMLulConvert(array){
        let html = []
        for(let i=0;i<array.length;i++){
        if(!(array[i] instanceof Array)){
            html.push(`<li>${array[i]}</li>`)
        }else{
            html.push(this.convert(array[i]))
        }
    }
    return `<ul>${html.join("")}</ul>`
}