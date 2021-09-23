FROM python:3.9.0

WORKDIR /home/
RUN echo 'secret'

RUN git clone https://github.com/hokoro/cheon01.git

WORKDIR /home/cheon01/



RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN pip install mysqlclient



EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=cheon_1.settings.deploy && python manage.py migrate --settings=cheon_1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=cheon_1.settings.deploy cheon_1.wsgi --bind 0.0.0.0:8000"]