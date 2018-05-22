# Se utiliza de base imagen de python con python 2.7
FROM python:3.6
ARG DJANGO_ENV

# Agregamos los requerimientos a la imagen
ADD requirements /app/requirements

# Asignamos el directorio de trabajo
WORKDIR /app/

# Instalar dependencias de python
RUN pip install -r requirements/$DJANGO_ENV.txt

# Crear usuario sin privilegios
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
USER app