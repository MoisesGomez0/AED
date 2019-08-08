function CSV(){
    this.generateRandomCSV = CSVGenerateRandomCSV;
}
    function CSVGenerateRandomCSV(){
        rows = [];
        r = random2int();
        for(i=0;i<r;i++){
            columns = [];
            c = random2int();
            for(j=0;j<c;j++){
                columns.push(random2int());
            }
            rows.push(columns.join(","));
        }
        return rows.join("<br><br>");
    }