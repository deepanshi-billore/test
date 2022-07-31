import pymongo
import certifi
ca=certifi.where()
client = pymongo.MongoClient("mongodb+srv://deepanshibillore:Iwonttellyou18@cluster0.7h4po.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

d={
    "name":"abc",
    "email":'abc@gmail.com',
    "surname":'def'
}
db1=client["omgotest"]
coll=db1['test']
coll.insert_one(d)