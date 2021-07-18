import sys
import redis
import csv
import operator

def read_and_insert(redis):
	try:
		reader = csv.reader(open('nomes-registados-2018.csv', newline=''), delimiter=' ', quotechar='|')
		for row in reader:
			data = ', '.join(row).split(',')
			redis.set('nomes-registados:' + data[0], data[2])
	except IndexError:
		f = sys.stdin.readlines()

def key_search():
	key = str(input("Search for ('Enter' for quit): "))
	return key

def  Search(redis, key):
	mapa = {}
	key_list = r.keys('nomes-registados:' + key + '*')
	for x in key_list:
		k = x.decode()
		value = r.get(k)
		mapa[k[17:]] = (int) (value.decode())
	sorted_map = sorted(mapa.items(), key=lambda x: x[1], reverse=True)
	for x in sorted_map:
		print(x[0])

if __name__ == "__main__":
	r = redis.Redis(host='localhost', port=6379, db=0)
	read_and_insert(r)
	while True:
		key = key_search()
		if len(key) == 0:
			break
		else:
			Search(r, key)