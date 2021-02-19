FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/djangoapp/src

#COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
WORKDIR /opt/services/djangoapp/src
#RUN pip install pipenv && pipenv install --system

# Add requirements.txt to the image
COPY requirements.txt /opt/services/djangoapp/src/requirements.txt
RUN pip install -r requirements.txt

COPY . /opt/services/djangoapp/src
## RUN cd webapp && python manage.py collectstatic --no-input


EXPOSE 8000
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "webapp", "core.wsgi:application"]

