

import redis

r1 = redis.Redis(host='localhost', port=6379)
r2 = redis.Redis(host='localhost', port=6380)
r3 = redis.Redis(host='localhost', port=6381)

# guardar datos en la particion 1
r1.set('item', 'casa')

# guardar datos en la particion 2

r2.set('item', 'gato')

# guardar datos en la particion 3

r3.set('item', 'perro')


## VErsion 
"""
import redis

r1 = redis.Redis(host='localhost', port=6379)
r2 = redis.Redis(host='localhost', port=6380)
r3 = redis.Redis(host='localhost', port=6381)

# guardar datos en la particion 1
r1.set('nombre', 'Juan')
r1.set('apellido', 'Perez')
r1.set('edad', '25')

# guardar datos en la particion 2

r2.set('nombre', 'Maria')
r2.set('apellido', 'Gomez')
r2.set('edad', '30')

# guardar datos en la particion 3

r3.set('nombre', 'Pedro')
r3.set('apellido', 'Gonzalez')
r3.set('edad', '35')

"""