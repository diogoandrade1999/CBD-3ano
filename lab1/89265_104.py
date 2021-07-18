import sys
import redis

def read_and_insert(redis):
	try:
		f = open('female-names.txt', 'r')
		count = 0
		for line in f:
			line = line.rstrip()
			redis.set('female-names:' + line, count)
			count += 1
		f.close()
	except IndexError:
		f = sys.stdin.readlines()

def key_search():
	return str(input("Search for ('Enter' for quit): "))

def  Search(redis, key):
	key_list = r.keys('female-names:' + key + '*')
	for x in key_list:
		print(x.decode()[13:])

if __name__ == "__main__":
	r = redis.Redis(host='localhost', port=6379, db=0)
	read_and_insert(r)
	while True:
		key = key_search()
		if len(key) == 0:
			break
		else:
			Search(r, key)
