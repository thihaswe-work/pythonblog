### Run this first

```sh
pipenv install
```

```sh
pipenv shell
```

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

```sh
python manage.py runserver
```

> SuperUserName : root
>
> Password : admin

> Username : user1
>
> Password : Password@1

### Nginx Conf for server

> Nginx Conf
> server {

    listen 80;
    server_name localhost;

    # Proxy requests to Django development server
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Serve static files
    location /static/ {
        alias C:/Users/fresh/Documents/projects/ths/pythonBlog/static/;
    }

    # Serve media files (user-uploaded files)
    location /media/ {
        alias C:/Users/fresh/Documents/projects/ths/pythonBlog/avatars/;
    }
    }
