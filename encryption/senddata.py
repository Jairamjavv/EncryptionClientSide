# import gridfs
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
#Deployement Database
client = MongoClient("mongodb://5c976e9a76210f38e183c35c:UtOtY8RDSRzO@db.optimuscp.io:37017/5c976e9a76210f38e183c35c")
db = client['5c976e9a76210f38e183c35c']

#Local Database
# client = MongoClient("mongodb://localhost:27017/Registration_details")
# db = client['Registration_details']
# fs = gridfs.GridFS(db)

def sendData(p, email):
    # with open('./encryptedKey.txt', 'rb') as fopen:
    #     fileID_eKey = fs.put(fopen.read())
    # with open('./encrypted.txt', 'rb') as fopen:
    #     fileID_ckey = fs.put(fopen.read())
    pids = db['pids']
    pid = ({
        'process_id' : p,
        'email':email
    })
    pids.insert_one(pid)