# ML Training

## Установка

Необходимо установить python2.7, postgres и heroku.

```sh
make
# Then activate virtual environment by instruction in output
# For Linux or OS X:
. venv/bin/activate
# For Windows (under Cygwin)
venv/Scripts/activate.bat
# For Windows (under Mingw)
. venv/Scripts/activate

# Then install requirements
make pip
```

## Деплой

1. После изменений коммитим и пушим.
1. Ждем пока приложение задеплоиться. Это происходит автоматически, примерно 3-5 минут.
1. Не забываем сделать удаленную миграцию:

    ```sh
    heroku run python manage.py migrate --app ml-training
    ```

    **Без этого изменения в модели не будут применены!**

## Локальный запуск

До запуска копируем `config.example.json` в новый файл `config.json` и обновляем информацию:

```sh
cd ml-training-website
cp config.example.json config.json
```

Для запуска приложения локально выполните одну из следующих команд:

```sh
heroku local web
```
or
```sh
make dev
```
or
```sh
python manage.py runserver 0.0.0.0:3000
```

Приложение будет запущено по адресу [localhost:3000](http://localhost:3000/).

### Деактивация virtualenv

Выполни:

```sh
deactivate
```

Если она не сработает, то пробуй с `source`:

```sh
source deactivate
```

## Переводы

Для переводов используем [стандартные средства Django](https://docs.djangoproject.com/en/1.9/topics/i18n/translation).

После того, как добавили какой-либо текст для перевода, необходимо выполнить следующую команду:

```sh
python manage.py makemessages
```

После этого необходимо в файле `ml_training/locale/en/LC_MESSAGES/django.po` произвести необходимые изменения с переводом. И выполнить:

```sh
python manage.py compilemessages -l en -l ru
```

После этого уже можно коммитить и пушить.

### Как добавить новый язык

1. В настройках в список `LANGUAGES` добавить необходимый ключ языка
1. Найти иконку с флагом для данного языка, желательно чтобы она была похожа на уже существующие `static/img/`
1. [Выполнить предыдущие шаги](#Переводы). Однако помните, что при компиляции необходимо добавить нужный ключ `-l`


## Документация

По информации об использовании Питона в Heroku заходи в девцентр:

- [Python для Heroku](https://devcenter.heroku.com/categories/python)

