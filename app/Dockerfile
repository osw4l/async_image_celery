# Se utiliza de base imagen de python con python 2.7
FROM ubuntu:16.04
ARG DJANGO_ENV

# Agregamos los requerimientos a la imagen
ADD requirements /app/requirements

# update repos
RUN apt-get update -y && apt-get upgrade -y

# instalar deps
RUN apt-get install -y build-essential libpq-dev \
	python3-dev libffi-dev python3-pip wget

RUN cd /tmp && \
    wget http://cairographics.org/releases/cairo-1.8.10.tar.gz && \
    tar xzf cairo-1.8.10.tar.gz && \
    cd cairo-1.8.10 && \
    PKG_CONFIG_PATH=/opt/lib/pkgconfig \
    LD_LIBRARY_PATH=/opt/lib \
    ./configure --prefix=/opt && \
    PKG_CONFIG_PATH=/opt/lib/pkgconfig \
    LD_LIBRARY_PATH=/opt/lib \
    make && \
    PKG_CONFIG_PATH=/opt/lib/pkgconfig \
    LD_LIBRARY_PATH=/opt/lib \
    make install


# Asignamos el directorio de trabajo
WORKDIR /app/

# Instalar dependencias de python
RUN sleep 30 && pip3 install -r requirements/$DJANGO_ENV.txt

# Crear usuario sin privilegios
RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
USER app
