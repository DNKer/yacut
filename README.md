# 	&#9986; YaCut. Укоротитель ссылок.

## Приложение, позволяющее ук(о)ротить любую длинную ссылку, превритив ее в удобочитаемую и воспринимаемую.

### &#128477; Ключевые возможности сервиса:
* генерация коротких ссылок, длиной от одного до шестнадцати символов, и связь их с исходными длинными ссылками
* переадресация на исходный адрес при обращении к коротким ссылкам

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
обязательного для длинной исходной ссылки;
необязательного для пользовательского варианта короткой ссылки. Все ссылки записываются и храняться в базе данных. Для тестовых (чебных) целей применена SQLite. При необходимости возможно подключить другую базу данных.

Проектом предусмотрен API, позволяющий POST-запросом создавать новую короткую ссылку и GET-запросомполучать оригинальную ссылку по указанному короткому идентификатору.

<img src="yacut\static\img\1649172105.png" alt="drawing"/>

## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=plastic&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=plastic&logo=Flask&logoColor=1008&color=008080)](https://flask.palletsprojects.com/en/latest/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=plastic&logo=GitHub%20actions&logoColor=1500C0&color=008080)](https://github.com/features/actions)
[![SQLite](https://img.shields.io/badge/-SQLite-464646?style=plastic&logo=SQLite&logoColor=80049C0&color=008080)](https://www.sqlite.org/index.html)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=plastic&logo=SQLAlchemy&logoColor=80049C0&color=008080)](https://www.sqlalchemy.org/)
![REST](https://img.shields.io/badge/-REST-464646?style=plastic&logo=REST&logoColor=80049C0&color=008080)

## Установка
> приводятся команды для `Windows`.

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/DNKer/yacut.git
```

```bash
cd yacut
```

Cоздать виртуальное окружение:

```bash
python -m venv venv
```

Активировать виртуальное окружение:

```bash
source venv/scripts/activate
```

Обновить систему управления пакетами:
```bash
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
flask db upgrade
```
__Репозиторий миграций создается один раз. Все созданные папки и файлы миграций становятся частью проекта и их нельзя игнорировать при работе с системами управления версий, например, с Git.__

Запустить проект:
```bash
flask run
```

Остановить проект:
```bash
flask run
```

## Создание новой бызы данных или работа с базой данных
Убедитесь, что вы находитесь в активированном окружении проекта и запустите в терминале интерактивную оболочку командой:
```bash
flask shell
```
Введите команды по очереди:
```bash
>>> from yacut import db

>>> db.create_all()

>>> exit()
```
Убедитесь что в корне проекта появился файл базы данных.

## Добавление данных (опционально) через интерактивную оболочку
```bash
>>> from yacut import URLMap

>>> url1 = URLMap(original='https://docs.sqlalchemy.org/en/20/orm/quickstart.html', short='sqlal1')

>>> db.session.add(url1)

>>> db.session.commit()
```
Поля ```id``` и ```timestamp``` заполнятся автоматически после того, как ссылки успешно добавилось в базу данных.

## Примеры работы API
#### Cоздание новой короткой ссылки:

```
POST /api/id/
```
```http
http://127.0.0.1:5000/api/id/
```
Тело:
```yuml
{
    "url": "https://flask.palletsprojects.com/en/latest/quickstart/#rendering-templates",
}
```
Ответ:
```yuml
{
    "short_link": "http://127.0.0.1:5000/18EXVC",
    "url": "https://flask.palletsprojects.com/en/latest/quickstart/#rendering-templates"
}
```
#### Получение оригинальной ссылки по указанному короткому идентификатору:
```
GET /api/id/<short_id>/
```
```http
http://127.0.0.1:5000/api/id/18EXVC
```
Тело пустое.

Ответ:
```yuml
{
    "url": "https://flask.palletsprojects.com/en/latest/quickstart/#rendering-templates"
}
```



#### Лицензия
###### Free Software, as Is 
###### _License Free_
###### Authors: [Dmitry](https://github.com/DNKer), [Yandex practikum](https://practicum.yandex.ru)
###### 2023