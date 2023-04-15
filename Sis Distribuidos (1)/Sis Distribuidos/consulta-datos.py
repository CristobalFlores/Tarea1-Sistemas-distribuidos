import redis

r1 = redis.Redis(host='localhost', port=6379)
r2 = redis.Redis(host='localhost', port=6380)
r3 = redis.Redis(host='localhost', port=6381)

# Consultar datos en la particion 1

dato1 = r1.get('item')
dato2 = r1.get('apellido')
dato3 = r1.get('edad')

# Consultar datos en la particion 2

dato4 = r2.get('item')
dato5 = r2.get('apellido')
dato6 = r2.get('edad')

# Consultar datos en la particion 3

dato7 = r3.get('item')
dato8 = r3.get('apellido')
dato9 = r3.get('edad')

# Imprimir datos

print(dato1)
print(dato2)
print(dato3)

print(dato4)
print(dato5)
print(dato6)

print(dato7)
print(dato8)
print(dato9)

