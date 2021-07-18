import redis

r = redis.Redis(host='localhost', port=6379, db=0)
print('Insert: ' + str(r.set('foo', 'bar')))
print('GET: ' + str(r.get('foo')))

