import redis

def menu():
	return input("\n1-Adicionar Utilizadores\n2-Associar jogadores\n3-Envio de Msg\n4-Leitura de Msg\n0-Sair\n>> ")

def adicionar(redis):
	name = input("\tNome: ")
	u = redis.lrange("lab1_1.5:names", 0, -1)
	if name.encode() not in u and len(name) != 0:
		redis.lpush("lab1_1.5:names", name)
		print("Sucesso!")
	else:
		if len(name) == 0:
			print("Nome inválido!")
		else:
			print("Utilizador já existe!")

def associar(redis):
	name1 = input("\tNome do seguidor: ")
	name2 = input("\tNome do utilizador a seguir: ")
	if name1 == name2:
		print("Não se pode associar o mesmo utilizador!")
	else:
		u = redis.lrange("lab1_1.5:names", 0, -1)
		if name1.encode() not in u or name2.encode() not in u:
			if name1.encode() not in u:
				print("Utilizador "+ name1 +" não existe!")
			if name2.encode() not in u:
				print("Utilizador "+ name2 +" não existe!")
		else:
			redis.lpush("lab1_1.5:seguir:" + name1, name2)
			print("Sucesso!")

def envio(redis):
	name = input("\tNome do utilizador: ")
	u = redis.lrange("lab1_1.5:names", 0, -1)
	if name.encode() not in u:
		print("Utilizador não existe!")
	else:
		msg = input("\tMensagem: ")
		redis.lpush("lab1_1.5:mensagens:" + name, msg)
		print("Sucesso!")

def leitura(redis):
	name = input("\tNome do utilizador: ")
	u = redis.lrange("lab1_1.5:names", 0, -1)
	if name.encode() not in u:
		print("Utilizador não existe!")
	else:
		msg = redis.lrange("lab1_1.5:mensagens:" + name, 0, -1)
		if msg:
			print("\tMsg de " + name + ":")
			for m in msg:
				print("\t\t" + m.decode())
		names = redis.lrange("lab1_1.5:seguir:" + name, 0, -1)
		for n in names:
			msg = redis.lrange("lab1_1.5:mensagens:" + n.decode(), 0, -1)
			if msg:
				print("\tMsg de " + n.decode() + ":")
				for m in msg:
					print("\t\t" + m.decode())
		print("Sucesso!")

if __name__ == "__main__":
	r = redis.Redis(host='localhost', port=6379, db=0)
	
	while True:
		m = menu()
		if m == '1':
			print("\nAdicionar Utilizador")
			adicionar(r)
		elif m == '2':
			print("\nAssociar jogadores")
			associar(r)
		elif m == '3':
			print("\nEnvio de Msg")
			envio(r)
		elif m == '4':
			print("\nLeitura de Msg")
			leitura(r)
		elif m == '0':
			print("\nSair")
			break
		else:
			print("Comando inexistente!")