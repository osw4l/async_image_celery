COMMAND=$1
docker-compose exec app python3 manage.py $COMMAND
