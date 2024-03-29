## Django boilerplate

## How to set up project

## How to run project locally bash script (Linux, Mac)

### install requirements

```bash
python3 -m venv env 
source env/bin/activate
pip install -r requirements/develop.text
```

### create .env file

```bash
cp .env.example .env
```

### create database

```bash
sudo -u postgres psql
CREATE DATABASE django_boilerplate;
CREATE USER django_boilerplate WITH PASSWORD 'django_boilerplate';
ALTER ROLE django_boilerplate SET client_encoding TO 'utf8';
ALTER ROLE django_boilerplate SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_boilerplate SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE django_boilerplate TO django_boilerplate;
\q
```

### set up .env file with your database credentials

```bash
nano .env
```

### run migrations

```bash
python manage.py migrate
```

### run server

```bash
python manage.py runserver

```


