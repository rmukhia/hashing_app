# Hashing Service

The form which generates the HTTP GET query parameter is at `/`.

The request logs is visible through the default `admin app` or through `/request_log`.

The database is a local sqllite3 file.

### Setup
```shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

### Run
```
$ python manage.py runserver
```

