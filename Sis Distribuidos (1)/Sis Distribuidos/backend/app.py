

### version 4 limpia

# backend/app.py
import json
import time
import threading
from flask import Flask
import requests
import redis

app = Flask(__name__)
client1 = redis.Redis(host='localhost', port=6379)  # Conexión a Redis 1
client2 = redis.Redis(host='localhost', port=6380)  # Conexión a Redis 2
client3 = redis.Redis(host='localhost', port=6381)  # Conexión a Redis 3

# Función para ejecutar la consulta a la API y actualizar el caché en Redis
def update_cache():
    dato1 = str(client1.get("item"))[2:-1]
    dato2 = str(client2.get("item"))[2:-1]
    dato3 = str(client3.get("item"))[2:-1]
    
    #threading.Timer(10.0, update_cache).start()  # Ejecutar la función cada 10 segundos
    do_query(dato1)
    do_query(dato2)
    do_query(dato3)
         

# Función para realizar la consulta a la API y actualizar el caché en Redis

def do_query(dato):
    start_time = time.time()
    
    
    if client1.hexists(dato,0):
        print (client1.hget(dato,0))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client1.hexists(dato,1):
        print (client1.hget(dato,1))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client1.hexists(dato,2):
        print (client1.hget(dato,2))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client2.hexists(dato,3):
        print (client2.hget(dato,3))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client2.hexists(dato,4):
        print (client2.hget(dato,4))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client2.hexists(dato,5):
        print (client2.hget(dato,5))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client3.hexists(dato,6):
        print (client3.hget(dato,6))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client3.hexists(dato,7):
        print (client3.hget(dato,7))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client3.hexists(dato,8):
        print (client3.hget(dato,8))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
    elif client3.hexists(dato,9):
        print (client3.hget(dato,9))
        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')

    else:

        try:
            response = requests.get('https://api.archivelab.org/items/'+dato)  # Realizar consulta a la API
            data = response.json()
            #created = response.get('created')
            print (data)
            item_id= str(data.get('created'))
            id = int(item_id[-1:])


            print (response)

            if id >= 0 and id <= 2:
                client1.hset(dato, id, json.dumps(data))
            elif id >= 3 and id <= 5:
                client2.hset(dato, id, json.dumps(data))
            elif id >= 6 and id <= 9:
                client3.hset(dato, id, json.dumps(data))
            
            elapsed_time = time.time() - start_time

            print(f'Tiempo de consulta: {elapsed_time} segundos')
            print('Cache actualizado en Redis')
        except Exception as e:
            print(f'Error al realizar la consulta: {e}')



# Iniciar el cronjob para actualizar el caché
start_time = time.time()
update_cache()

elapsed_time = time.time() - start_time
print(f'Tiempo de consulta: {elapsed_time} segundos')

# Ruta para realizar la consulta a la API
@app.route('/consulta')



def consulta():
    start_time = time.time()
    try:
        # Obtener datos del caché de Redis, si no existen, realizar consulta a la API y almacenar en los cachés
        items = {}
        for i in range(30):
            if i >= 0 and i <= 9:
                item = client1.hget('consulta', i)
            elif i >= 10 and i <= 19:
                item = client2.hget('consulta', i)
            elif i >= 20 and i <= 29:
                item = client3.hget('consulta', i)

            if item:
                items[i] = json.loads(item.decode('utf-8'))

        elapsed_time = time.time() - start_time
        print(f'Tiempo de consulta: {elapsed_time} segundos')
        return json.dumps(items)
    except Exception as e:
        print(f'Error al realizar la consulta: {e}')
        return {'error': 'Error al realizar la consulta'}, 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

