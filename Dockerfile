# Usa una imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo en el contenedor
WORKDIR /yakuza-bot

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del bot al contenedor
COPY . .

# Define el comando para ejecutar el bot
CMD ["python", "bot.py"]
