# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /lib/Pacientes

# Copia los archivos del proyecto al contenedor
COPY . /lib/Pacientes

# Agrega el directorio raíz al PYTHONPATH para que Python pueda encontrar los módulos correctamente
ENV PYTHONPATH="/usr/lib:$PYTHONPATH"

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "lib.Medico.run:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
