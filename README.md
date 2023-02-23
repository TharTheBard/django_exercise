# Django exercise
Rest API and database for as an exercise for Whys.

## How to run
```
cd docker/
docker-compose up --build -d
```
If this is the first time you need to run these as well
```
docker-compose exec django-exercise python manage.py makemigrations
docker-compose exec django-exercise python manage.py migrate
```

- Once running you can:
  - Server runs at 0.0.0.0:8000

  - REST Api try out routes are available at paths:
    - /import/
    - /detail/<model_name>/
    - /detail/<model_name>/<pk>/
    
  - View logs at:
    ```
    tail -f log/syslog
    ```
    
  - Browse database via:
    ```
    docker exec -it docker_db_1 psql -U postgres
    ```