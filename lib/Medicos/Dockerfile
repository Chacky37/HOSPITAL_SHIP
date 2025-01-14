# Utiliza una imagen base de Python
FROM python:3.9.21-alpine3.21

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación
COPY . /app

# Expone el puerto en el que la aplicación escuchará
EXPOSE 3700

# Comando para ejecutar la aplicación
CMD ["uvicorn", "lib.Medicos.run:app", "--host", "0.0.0.0", "--port", "3700", "--reload"]

