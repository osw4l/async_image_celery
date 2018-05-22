# SERVER /opt/app/

# MONTAR ENTORNO POR PRIMERA VEZ

	# CONFIGURAR VARIABLES DE ENTORNO
	cp env.template .env

	# EJEMPLO DE .env

	LANG=C.UTF-8
	LC_ALL=C.UTF-8
	SECRET_KEY=#DJANGO SECRET_KEY
	DEBUG=false
	HTTPS=on
	POSTGRES_DB=#NOMBRE QUE SE QUIERE DAR A LA BASE DE DATOS
	POSTGRES_USER=#USUARIO
	POSTGRES_PASSWORD=#PASSWORD
	SUBDIR_PATH=mahou_v2
	BIGTINCAN_CLIENT_ID=#CLIENT ID
	BIGTINCAN_CLIENT_SECRET=#CLIENT SECRET
	BIGTINCAN_ADMIN_USERNAME=#BIGTINCAN EMAIL ADMIN
	BIGTINCAN_ADMIN_PASS=#BIGTINCAN PASS ADMIN
	BIGTINCAN_API_DOMAIN=#DOMAIN
	BIGTINCAN_API_LIMIT=#ITEM POR PAGINAS

	# CREAR IMAGENES PARA NAUTY360
	docker-compose -f prod.yml build

# INICIAR SERVIDOR DE NAUTY360

docker-compose -f prod.yml up -d

# CREAR EL MODELO DE DATOS EN LA BASE DE DATOS

docker-compose -f prod.yml exec app python manage.py makemigrations
docker-compose -f prod.yml exec app python manage.py migrate

# REINICIAR LOS SERVICIOS PARA QUE CARGUE CORRECTAMENTE CELERY

docker-compose -f prod.yml restart beat

# COMPROBAR EL ESTADO DEL BACKEND

docker-compose -f prod.yml ps

# CREAR UN USUARIO ADMINISTRADOR EN NUESTRO BACKEND

docker-compose -f prod.yml exec app python manage.py createsuperuser


# show logs
docker-compose logs -f app

# estado de los procesos
docker-compose ps