COMMAND=$1
docker-compose exec app python manage.py $COMMAND
