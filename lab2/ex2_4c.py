import pymongo
import datetime

client = pymongo.MongoClient('localhost',27017)
db = client.cbd
collection = db.rest


def count_localidades():
    query = collection.aggregate(
    [{"$group": {"_id": "$localidade", "total": {"$sum": 1}}}])
    return len(list(query))


def count_localidade():
    query = collection.aggregate(
    [{"$group": {"_id": "$localidade", "total": {"$sum": 1}}}])
    return [(entry["_id"], entry["total"]) for entry in list(query)]


def count_localidade_gastronomia():
    query = collection.aggregate(
    [{"$group": {"_id": {"localidade": "$localidade", "gastronomia": "$gastronomia"}, "total": {"$sum": 1}}}])
    return [(f"{entry['_id']['localidade']} | {entry['_id']['gastronomia']}", entry["total"]) for entry in list(query)]


def get_collection_with_name_closer_to(name):
    query = collection.find({"nome": {"$regex": name}})
    return [entry["nome"] for entry in list(query)]


if __name__ == "__main__":
    print(f"Número de localidades distintas: {count_localidades()}")
    print("\nNúmero de localidades distintas:")
    for count in count_localidade():
        print(f"  -> {count[0]}: {count[1]}")
    print("\nNúmero de restaurantes por localidade e gastronomia:")
    for count in count_localidade_gastronomia():
        print(f"  -> {count[0]}: {count[1]}")
    print("\nNome de restaurantes que têm 'Park' no nome: ")
    for collection in get_collection_with_name_closer_to("Park"):
        print(f"  -> {collection}")
