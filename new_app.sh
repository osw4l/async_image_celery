APP=$1
docker-compose exec app python3 manage.py startapp $APP
echo 'nueva app creada '$APP