import redis

class SimplePost:
	def __init__(self):
		self.redis = redis.Redis(host='localhost', port=6379, db=0)
		self.USERS_SET = 'users1.3_set'
		self.USERS_LIST = 'users1.3_list'
		self.USERS_HASH = 'users1.3_hash'
		
	def saveUserSet(self, username):
		self.redis.sadd(self.USERS_SET, username)

	def getUserSet(self):
		return self.redis.smembers(self.USERS_SET)

	def getAllKeysSet(self):
		return self.redis.keys(self.USERS_SET)

	def saveUserList(self, username):
		self.redis.lpush(self.USERS_LIST, username)

	def getUserList(self):
		return self.redis.lrange(self.USERS_LIST, 0, -1)

	def getAllKeysList(self):
		return self.redis.keys(self.USERS_LIST)

	def saveUserHash(self, username):
		self.redis.hmset(self.USERS_HASH, username)

	def getAllUserHash(self):
		return self.redis.hgetall(self.USERS_HASH)

	def getAllKeysHash(self):
		return self.redis.keys(self.USERS_HASH)

	def deleteKeysList(self):
		self.redis.delete(self.USERS_LIST)


if __name__ == "__main__":
	board = SimplePost();
	board.deleteKeysList()
	users = ["Ana", "Pedro", "Maria", "Luis"]
	map_users = {}
	for user in users:
		board.saveUserSet(user)
		board.saveUserList(user)
		map_users['name' + str(users.index(user))] = user
	board.saveUserHash(map_users)
	print(board.getAllKeysSet()[0].decode())
	for users in board.getUserSet():
		print(users.decode())
	print(board.getAllKeysList()[0].decode())
	for users in board.getUserList():
		print(users.decode())
	print(board.getAllKeysHash()[0].decode())
	for key, value in board.getAllUserHash().items():
		print(key.decode() + ': ' + value.decode())
