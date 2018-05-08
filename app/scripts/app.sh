#!/bin/bash
chown -R app:app /app/media
su - app
mkdir /home/app/logs > /dev/null 2>&1

touch /home/app/logs/gunicorn-access.log
touch /home/app/logs/gunicorn.log
#touch /home/app/logs/app.log
tail -n 0 -f /home/app/logs/*.log &

#python manage.py migrate
python manage.py collectstatic --clear --noinput > /dev/null 2>&1
python manage.py collectstatic --noinput > /dev/null 2>&1

exec gunicorn $PROJECT_NAME.wsgi -b :8000 \
	--access-logfile /home/app/logs/gunicorn-access.log \
	--error-logfile /home/app/logs/gunicorn.log
