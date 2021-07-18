import pymongo
import datetime

client = pymongo.MongoClient('localhost',27017)
db = client.cbd
collection = db.rest

collection.create_index("localidade", name='localidade')
collection.create_index("gastronomia", name='gastronomia')
collection.create_index([("nome", pymongo.TEXT)], name='nome')
print(collection.index_information())
