import pymongo
import datetime

client = pymongo.MongoClient('localhost',27017)
db = client.cbd
collection = db.rest

def main():
	return input('1-insert\n2-edit\n3-search\n0-sair\n>>')

def insert():
	address_building = input('address_building: ')
	address_coord_latitude = int(input('address_coord_latitude: '))
	address_coord_longitude = int(input('address_coord_longitude: '))
	address_rua = input('address_rua: ')
	address_zipcode = input('address_zipcode: ')
	localidade = input('localidade: ')
	gastronomia = input('gastronomia: ')
	# datetime.datetime(2011, 10, 4, 16, 46, 59, 786000)
	date = input('grades_date: ').split('-')
	year = int(date[0])
	month = int(date[1])
	day = int(date[2])
	grades_date = datetime.datetime(year, month, day)
	grades_grade = input('grades_grade: ')
	grades_score = input('grades_score: ')
	nome = input('nome: ')
	restaurant_id = input('restaurant_id: ')

	mydict = {
				"address" : {
					"building" : address_building,
					"coord" : [
						address_coord_latitude,
						address_coord_longitude
					],
					"rua" : address_rua,
					"zipcode" : address_zipcode
				},
				"localidade" : localidade,
				"gastronomia" : gastronomia,
				"grades" : [
					{
						"date" : grades_date,
						"grade" : grades_grade,
						"score" : grades_score
					}
				],
				"nome" : nome,
				"restaurant_id" : restaurant_id
			}

	x = collection.insert_one(mydict)
	# x = mycol.insert_many(mylist)


def edit():
	update = {"localidade": "Acores"}
	values = {"$set": {"localidade": "Aveiro"}}
	result = collection.update_many(update, values)


def search():
	for x in collection.find():
		print(x)

if __name__ == '__main__':
	while True:
		e = main()
		if e == '1':
			insert()
		elif e == '2':
			edit()
		elif e == '3':
			search()
		elif e == '0':
			break
		else:
			print("Command don't exit!")
