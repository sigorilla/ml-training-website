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

## Локальный запуск

До запуска копируем `config.example.json` в новый файл `config.json` и обновляем информацию:

```sh
cd ml-training-website
cp config.example.json config.json
```

Для запуска приложения локально выполните одну из следующих команд:

```sh
$ heroku local web
```
or
```sh
$ make dev
```
or
```sh
$ python manage.py runserver 0.0.0.0:3000
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


## Документация

По информации об использовании Питона в Heroku заходи в девцентр:

- [Python для Heroku](https://devcenter.heroku.com/categories/python)

