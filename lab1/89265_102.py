import sys

if __name__ == "__main__":
	try:
		filename = sys.argv[1]
		f = open(filename, 'r')
	except IndexError:
		f = sys.stdin.readlines()

	lista = []
	letra = ''
	for line in f:
		line = line.rstrip()
		if letra == line[0] or letra == '':
			lista.append(line)
			letra = line[0]
		else:
			print(" SET " + letra.upper() + " " + str(len(lista)))
			lista = []
			letra = ''

	f.close()