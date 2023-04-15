# Testeo de Api, para ver si presenta algun bloqueo de consulta

import requests
import time
import matplotlib.pyplot as plt

# Funcion para obtener el tiempo de respuesta de la api
url= "https://api.archivelab.org/items/"
tiempos = []


def getResponseTime(url):
    start = time.time()
    requests.get(url + str(i))
    end = time.time()
    return end - start

# imprimir valores de la API
# print(response.json())

# Se realiza 100 consultas a la api
for i in range(1,5001):
    start_time = time.time()
    response = requests.get(url + str(i))
    end_time = time.time()

    tiempo_consulta = end_time - start_time
    tiempos.append(tiempo_consulta)
    print(str(i)+" Tiempo de respuesta: {}".format(tiempo_consulta) + "  Segundos")
    print(response)
    print(response.json())
    contador = i

tiempo_total = time.time() - start_time
print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")
### print("Tiempo total de ejecucion: {}".format(tiempo_total) + "  Segundos")

#imprimir el total de consultas hechas
print("Total de consultas realizadas: {}".format(contador))
#suma total de los tiempos de las 100 consultas
sum = sum(tiempos)
print("La suma de los tiempos de respuesta es: {}".format(sum) + "  Segundos")
#imprimir en minutos
print("La suma de los tiempos de respuesta es: {}".format(sum/60) + "  Minutos")
#imprimir en horas
print("La suma de los tiempos de respuesta es: {}".format(sum/3600) + "  Horas")

print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")

# promedio del tiempo de las 100 consultas realizadas
promedio1 = float(sum/contador)
print("El promedio de los tiempos de respuesta es: {}".format(promedio1) + "  Segundos")

print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")

# Se grafica el tiempo de respuesta de la api
plt.plot(range(1,contador+1),tiempos)
plt.ylabel('Tiempo de respuesta')
plt.xlabel('Numero de consulta')
plt.title("Tiempos de consulta API")
plt.show()



# Se obtiene el tiempo de respuesta de la api
# responseTime = getResponseTime(url)
# print(responseTime)



