from cassandra.cluster import Cluster
from datetime import date


cluster = Cluster()
session = cluster.connect('ex3_2')

def alinea_b():
	print('---------------b----------------')
	rows = session.execute('SELECT * FROM comentarios WHERE id_video=1 ORDER BY selo_temporal DESC LIMIT 3;')
	print('SELECT * FROM comentarios WHERE id_video=1 ORDER BY selo_temporal DESC LIMIT 3;')
	for c in rows:
		print(f'{c.id_video}, {c.selo_temporal}, {c.autor}, {c.content}')
	print('--------------------------------')
	rows = session.execute('SELECT autor FROM followers WHERE id_video=1 ;')
	print('SELECT autor FROM followers WHERE id_video=1 ;')
	for c in rows:
		print(f'{c.autor}')
	print('--------------------------------')
	rows = session.execute("Select * from videos where tag contains '#new';")
	print("Select * from videos where tag contains '#new';")
	for c in rows:
		print(f'{c.id}, {c.autor}, {c.descricao}, {c.nome}, {c.selo_temporal}, {c.tag}')

def select():
	print('SELECT--------------------------')
	rows = session.execute('SELECT * FROM utilizadores')
	for user_row in rows:
		print(f'{user_row.username}, {user_row.nome}, {user_row.email}, {user_row.selo_temporal}')

def insert():
	print('INSERT--------------------------')
	session.execute(
	    """
	    INSERT INTO utilizadores (username, nome, email, selo_temporal)
	    VALUES (%s, %s, %s, %s)
	    """,
	    ('john', "John Dead", 'john@mail.uk', date.today())
	)

def delete():
	print('DELETE--------------------------')
	session.execute("DELETE FROM utilizadores WHERE username='john'")

def update():
	print('UPDATE--------------------------')
	session.execute("UPDATE utilizadores SET nome = 'King John' WHERE username='john'")

select()
insert()
select()
update()
select()
delete()
alinea_b()
