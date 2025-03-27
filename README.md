# RESTI CRM

BACKEND STACK

- [in_progress] FastAPI
- [done] PostgreSQL
- [in_progress] Redis
- [in_progress] Redis

FRONTEND STACK

- [in_progress] ReactJS

DEVOPS STACK

- [done] Traefik
- [in_progress] auto certbot ssl

Setting environment for backend development

```shell
cd backend
python -m venv .venv
source ./.venv/bin/activate
pip install poetry
poetry install --no-root --no-ansi --with=dev 
```

Local dev deploy

```shell
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py run
```

Docker deploy. [Requires .env file]

```shell
docker compose up
```
