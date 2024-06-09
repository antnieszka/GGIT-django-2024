# GGIT-django-2024

Instalacja zależności za pierwszym razem
```shell
pip install -r requirements.txt
```

Uruchomienie serwera
```shell
python manage.py runserver
```

Generowanie migracji bazy danych po zmianie models.py
```shell
python manage.py makemigrations
```

Aktualizacja bazy danych (aplikowanie migracji, wymagane po wygenerowaniu migracji)
```shell
python manage.py migrate
```

Tworzenie superusera (admina)
```shell
python manage.py createsuperuser
```
