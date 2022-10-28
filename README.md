# Creating environment

```
git init
git clone https://github.com/Simple2B/School-portal.git
cd School-portal
poetry install
cp sample.env .env
```

# Launch an run application locally

```
source .venv/bin/activate
python manage.py migrate
python manage.py runserver
```
