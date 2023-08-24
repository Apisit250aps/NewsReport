# NewsReport
- [NewsReport](#newsreport)
  - [What can to do?](#what-can-to-do)
  - [Project Information.](#project-information)
- [Database.](#database)
  - [Install `psycopg` for connect to postgres SQL Server.](#install-psycopg-for-connect-to-postgres-sql-server)
  - [Setting Database connection to postgres SQL Server.](#setting-database-connection-to-postgres-sql-server)
  - [Dump and Load database to JSON file.](#dump-and-load-database-to-json-file)
    - [install Django Dump Load UTF-8 for windows.](#install-django-dump-load-utf-8-for-windows)
    - [Add to INSTALL\_APPS. settings.py](#add-to-install_apps-settingspy)
    - [Dumpdata to JSON command.](#dumpdata-to-json-command)
    - [Loaddata to new database command.](#loaddata-to-new-database-command)
  - [Entity Relations Diagram ( ERD ).](#entity-relations-diagram--erd-)
- [Webpage](#webpage)
  - [feeds](#feeds)
  - [read](#read)
  - [admin](#admin)
- [Developments](#developments)
  - [COPY settings.py](#copy-settingspy)
  - [COPY manage.py](#copy-managepy)

## What can to do?
- App for reading articles or news.
- News or article can be added from the admin page.
  
## Project Information.
- Django Framework.
- Bootstrap 5 Templates.
- Postgres SQL.
- [Requirements](./requirements.txt)

# Database.
## Install `psycopg` for connect to postgres SQL Server.
```
pip install psycopg2
```
## Setting Database connection to postgres SQL Server.
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "<database name>",
        "USER": "<username>",
        "PASSWORD": "<password>",
        "HOST": "<host>",
        "PORT": "<port>",
    }
}
```

## Dump and Load database to JSON file.
### install Django Dump Load UTF-8 for windows.
```
pip install django-dump-load-utf8
```


### Add to INSTALL_APPS. [settings.py](/news_writer/settings.py)
```python
INSTALLED_APPS = [
    '...',
    'django_dump_load_utf8',
    '...',
]
```
### Dumpdata to JSON command.
```
python manage.py dumpdatautf8 --output data.json
```
### Loaddata to new database command.

```
python manage.py loaddatautf8 data.json
```
## Entity Relations Diagram ( ERD ).

```
entity Category {
  id: integer PK
  category: string
}

entity Author {
  id: integer PK
  user: integer FK > User
  profile_img: string
  occupation: string
  follower: integer
  description: string
  category: integer FK > Category
  verify: boolean
}

entity Follow {
  id: integer PK
  author: integer FK > Author
  user: integer FK > User
  follow_date: datetime
}

entity Content {
  id: integer PK
  author: integer FK > Author
  poster: string
  title: string
  description: string
  detail: string
  like: integer
  read: integer
  write: datetime
}

entity Comment {
  id: integer PK
  user: integer FK > User
  content: integer FK > Content
  detail: string
  like: integer
}

entity ReplyComment {
  id: integer PK
  user: integer FK > User
  comment: integer FK > Comment
  detail: string
  link: integer FK > Comment
}

relationship Author{
  author }--{ content }
  author }--{ category }
  author }--{ follow }
}

relationship Content{
  content }--{ comment }
  content }--{ replyComment }
}

relationship User{
  user }--{ follow }
}

relationship Comment{
  comment }--{ replyComment }
}

```

# Webpage
## feeds
![image](/screen/feeds.png)
*A page for displaying all news content information, such as a list of authors, news or articles, divided by content type.*
## read 
![image](/screen/reads.png)
*A page for reading news and articles. and will display other content of the same author or same category*
## admin
![image](/screen/admin.png)
*Admin page for writing news or content and can also add authors and categories.*


# Developments
## COPY settings.py
```
COPY settings.py settings_dev.py
```

## COPY manage.py
```
COPY manage.py manage_dev.py
```

*edit manage_dev.py*
```python 

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_writer.settings_dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

```