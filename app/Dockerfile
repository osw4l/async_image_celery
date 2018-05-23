# Se utiliza de base imagen de python con python 2.7
FROM ubuntu:16.04
ARG DJANGO_ENV

# Agregamos los requerimientos a la imagen
ADD requirements /app/requirements

# Asignamos el directorio de trabajo
WORKDIR /app/

# update repos
RUN apt-get update -y

# instalar deps
RUN apt-get install -y build-essential libpq-dev \
	python3-dev libffi-dev python3-pip

# Instalar dependencias de python
RUN pip3 install -r requirements/$DJANGO_ENV.txt

# Crear usuario sin privilegios
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
USER app
