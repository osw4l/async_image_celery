# SERVER /opt/app/

# MONTAR ENTORNO POR PRIMERA VEZ

# CONFIGURAR VARIABLES DE ENTORNO
cp env.template .env


# CREAR IMAGENES PARA UPLOADER
nano .env # para configurar las variables
docker-compose build

# INICIAR SERVIDOR DE UPLOADEr

docker-compose up -d

# MIGRACIONES

sudo chmod u+x migrate_db.sh

./migrate_db.sh


# REINICIAR LOS SERVICIOS PARA QUE CARGUE CORRECTAMENTE CELERY

docker-compose down
docker-compose up -d

# COMPROBAR EL ESTADO DEL BACKEND

docker-compose ps

# CREAR UN USUARIO

docker-compose exec app python manage.py createsuperuser

# OTRA FORMA

sudo chmod u+x create_user.sh
./create_user.sh

# LIBRERIA PARA LA AUTENTICACION

http://django-rest-auth.readthedocs.io/en/latest/

# CLOUD STORAGE PARA IMAGENES

https://cloudinary.com/documentation/django_integration

# URL PARA EL ADMIN DE DJANGO
http://localhost:8000/api-manager/

# END POINT PARA LOGIN
http://localhost:8000/rest-auth/login/
# recibe
{
	"username":"user",
	"password":"password",
	"email":""
}

# RETORNA UN KEY QUE SE DEBE MANDAR DE LA SIGUIENTE MANERA
-> Authorization   Token 79c6babdcdafa50b994c39804676131c068d362d

# PARA SUBIR UNA O MUCHAS IMAGENES HASTA 50MB, CONFIGURADO EN NGINX VIA POST
http://localhost:8000/api/viewsets/images/ # <- recibe datos en form data

# PARA VER LOS TICKETS HAY DOS ENPOINTS todas responden a get
http://localhost:8000/api/tickets/ 
http://localhost:8000/api/viewsets/images/
http://localhost:8000/api/viewsets/tickets-images


