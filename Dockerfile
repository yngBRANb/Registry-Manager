FROM python:3.11

WORKDIR /app

COPY req.txt .

RUN pip install -r req.txt

COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8080

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]