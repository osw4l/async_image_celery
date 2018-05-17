APP=$1
docker-compose exec app python manage.py startapp $APP
