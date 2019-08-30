def deep(json,tab=""):
    for k,value in json.items():
        if isinstance(value,dict):
            print("%s%s"%(tab,k))
            deep(value,"%s%s" %(tab,"\t"))
        else:
            print("%s%s:%s"%(tab,k,value))

json = {"root":{
        "archivo1":{
            "type":"file",
            "size":804,
            "author":"Grupo niche",
            "extension":"mp3",
            "date":"2019/05/44"
        },
        "archivo1/":{
            "type":"folder",
            "size":4,
            "user":"mg",
            "children":{
                    "archivo1":{
                "type":"file",
                "size":804,
                "author":"Grupo niche",
                "extension":"mp3",
                "date":"2019/05/44"
                }   
            }
        }
    }
}
deep(json)