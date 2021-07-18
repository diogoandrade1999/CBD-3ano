from py2neo.data import Node, Relationship
import random
import pprint

persons = []
teams = []

f= open('persons.txt', 'r');
for line in f:
	persons.append(f.readline()[:-1])
f.close()

f= open('teams.txt', 'r');
for line in f:
	teams.append(f.readline()[:-1])
f.close()


persons_node = []
teams_node = []

for p in persons:
	persons_node.append(Node("Person", name=p, age=random.randint(18, 50)))
pprint.pprint(persons_node)

for t in teams:
	teams_node.append(Node("Team", name=t))
pprint.pprint(teams_node)


teams_rel = []

for p in persons_node:
	for x in range(random.randint(1, 5)):
		a = random.choice(teams_node)
		r = Relationship(p, "PLAY/PLAYED ON", a)
		if r not in teams_rel:
			teams_rel.append(r)
pprint.pprint(teams_rel)


play_rel = []
reverse_play_rel = []

while len(play_rel) < 500:
	a = random.choice(persons_node)
	b = random.choice(persons_node)
	r = Relationship(a, "PLAY WITH", b)
	if r not in play_rel or r not in reverse_play_rel:
		play_rel.append(r)
		reverse_play_rel.append(Relationship(b, "PLAY WITH", a))
pprint.pprint(play_rel)


f= open('CBD_L44c_89265.txt', 'w');
for p in persons_node:
	f.write(str(p)+'\n')
for t in teams_node:
	f.write(str(t)+'\n')
for tr in teams_rel:
	f.write(str(tr)+'\n')
for pr in play_rel:
	f.write(str(pr)+'\n')
f.close()
