# Imagen base
FROM python:3.9

# Directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al directorio de trabajo
COPY app.py /app
COPY requerimientos.txt /app

# Instalar las dependencias
RUN pip install -r requerimientos.txt

# Exponer el puerto 3000 para la aplicación Flask
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
















##TEST 1



# Utiliza una imagen de Python
#FROM python:3.9

# Establece el directorio de trabajo en /app
#WORKDIR /app

# Copia el archivo requirements.txt al contenedor
#COPY requerimientos.txt .

# Instala las dependencias del backend
#RUN pip install -r requerimientos.txt

# Copia el código fuente del backend al contenedor
#COPY app.py .

# Expone el puerto 3000 para el backend
#EXPOSE 3000

# Inicia la aplicación del backend
#CMD ["python", "app.py"]






