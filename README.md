<!-- <style>
@font-face {
    font-family: 'monospace';
    unicode-range: U+41-5A, U+61-7A, U+C0-FF;
}
@font-face {
    font-family: 'Kanit';
    unicode-range: U+0E00–U+0E7F;
}

h1, h2, h3, h4, h5, h6, p,a , li{
    font-family:  'Kanit';
}

h1, h2, h3, h4, h5, h6 {
  font-weight:200;
}

p, a, li {
  font-weight:200;
}


</style> -->

# NewsReport
- [NewsReport](#newsreport)
  - [ทำอะไรได้บ้าง](#ทำอะไรได้บ้าง)
  - [รายละเอียดโปรเจค](#รายละเอียดโปรเจค)
- [ระบบฐานข้อมูล](#ระบบฐานข้อมูล)
  - [ติดตั้ง `psycopg2` สำหรับการเชื่อมต่อไปยัง postgres SQL Server.](#ติดตั้ง-psycopg2-สำหรับการเชื่อมต่อไปยัง-postgres-sql-server)
  - [การตั้ังค่าการเชื่อมต่อฐานข้อมูลไปยัง postgres SQL Server. `settings.py`](#การตั้ังค่าการเชื่อมต่อฐานข้อมูลไปยัง-postgres-sql-server-settingspy)
  - [ทำการ Migrate database เพื่อสร้างตารางทั้งหมดให้ฐานข้อมูลใหม่](#ทำการ-migrate-database-เพื่อสร้างตารางทั้งหมดให้ฐานข้อมูลใหม่)
  - [Dump and Load database to JSON file.](#dump-and-load-database-to-json-file)
    - [ติดตั้ง Django Dump Load UTF-8 สำหรับ windows.](#ติดตั้ง-django-dump-load-utf-8-สำหรับ-windows)
    - [เพิ่มใน INSTALL\_APPS. settings.py](#เพิ่มใน-install_apps-settingspy)
    - [คำสั่งสำหรับการ dumpdata และ loaddata](#คำสั่งสำหรับการ-dumpdata-และ-loaddata)
    - [Loaddata to new database command.](#loaddata-to-new-database-command)
  - [Entity Relations Diagram](#entity-relations-diagram)
- [หน้าเว็บ](#หน้าเว็บ)
  - [ฟีด](#ฟีด)
  - [การจัดหมวดหมู่](#การจัดหมวดหมู่)
  - [อ่าน](#อ่าน)
  - [แอดมิน](#แอดมิน)
- [การพัฒนา](#การพัฒนา)
  - [คัดลอกไฟล์ settings.py](#คัดลอกไฟล์-settingspy)
  - [คัดลอกไฟล์ manage.py](#คัดลอกไฟล์-managepy)
  - [เข้าไปแก้ไขไฟล์ `manage_dev.py` เพื่อให้เรียกใช้ ไฟล์ `settings_dev.py`](#เข้าไปแก้ไขไฟล์-manage_devpy-เพื่อให้เรียกใช้-ไฟล์-settings_devpy)




## ทำอะไรได้บ้าง
- อ่านเนื้อหาบทความ
- ค้าหาเนื้อหาบทความ
- จัดกลุ่มบทความด้วยหมวดหมู่
- จัดกลุ่มบลความด้วยผู้เขียนบทความ
- เขียนบทความในหน้าแอดมิน
- มีระบบ ผู้ใข้ธรรมดา (ผู้อ่านข่าว), ผู้เขียนข่าว
  
## รายละเอียดโปรเจค
- Django Framework.
- Bootstrap 5 Templates.
- Postgres SQL.
- [Requirements](./requirements.txt)

# ระบบฐานข้อมูล
## ติดตั้ง `psycopg2` สำหรับการเชื่อมต่อไปยัง postgres SQL Server.
```
pip install psycopg2
```
## การตั้ังค่าการเชื่อมต่อฐานข้อมูลไปยัง postgres SQL Server. `settings.py`

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
เปลี่ยนจากการเชื่อมต่อฐานข้อมูลแบบ Local เป็นระบบ Server

## ทำการ Migrate database เพื่อสร้างตารางทั้งหมดให้ฐานข้อมูลใหม่
```
python manage.py migrate
```

## Dump and Load database to JSON file.

เป็นการทำให้ข้อมูลในฐานข้อมูลอยู่ในรูปแบบ JSON เพื่อให้สามารถย้ายฐานข้อมูลได้
### ติดตั้ง Django Dump Load UTF-8 สำหรับ windows.

- ใช้สำหรับการโอนย้ายจากฐานข้อมูลเดิม ไปยังฐานข้อมูลใหม่


```
pip install django-dump-load-utf8
```

### เพิ่มใน INSTALL_APPS. [settings.py](/news_writer/settings.py)




```python
INSTALLED_APPS = [
    '...',
    'django_dump_load_utf8',
    '...',
]
```
### คำสั่งสำหรับการ dumpdata และ loaddata

```
python manage.py dumpdatautf8 --output data.json
```
*>>> ทำให้ข้อมูลอยู่ในรูปแบบ JSON*


### Loaddata to new database command.

```
python manage.py loaddatautf8 data.json
```
*>>> นำข้อมูลที่อยู่ในรูปแบบ JSON และ load ไปยังฐานข้อมูลใหม่*

## Entity Relations Diagram
```
entity Category {
  id: integer PK
  category: string
  img: string
}

entity Author {
  id: integer PK
  user: string FK
  profile_img: string
  occupation: string
  description: string
  verify: boolean
}

entity Content {
  id: integer PK
  author: integer FK
  poster: string
  title: string
  description: string
  detail: string
  read: integer
  category: integer FK
  write: datetime
}

entity Follow {
  id: integer PK
  author: integer FK
  user: integer FK
  follow_date: datetime
}

entity Like {
  id: integer PK
  content: integer FK
  user: integer FK
}

entity Comment {
  id: integer PK
  user: integer FK
  content: integer FK
  detail: string
  like: integer
}

entity ReplyComment {
  id: integer PK
  user: integer FK
  comment: integer FK
  detail: string
  like: integer
}

relationship "One to many" between Category and Content {
  Category {id} -> Content {category}
}

relationship "One to one" between Author and Content {
  Author {id} -> Content {author}
}

relationship "Many to many" between User and Follow {
  User {id} -> Follow {user}
  Follow {author} -> Author {id}
}

relationship "Many to one" between Content and Like {
  Content {id} -> Like {content}
  Like {user} -> User {id}
}

relationship "One to many" between Content and Comment {
  Content {id} -> Comment {content}
  Comment {user} -> User {id}
}

relationship "One to many" between Comment and ReplyComment {
  Comment {id} -> ReplyComment {comment}
  ReplyComment {user} -> User {id}
}

```


# หน้าเว็บ

## ฟีด
![image](/screen/feeds1.png)
![image](/screen/feeds2.png)
*เป็นหน้าการแนะนำเนื้อหา, ผู้เขียน และหมวดหมู่ทั้งหมด*


## การจัดหมวดหมู่

![image](/screen/category.png)
*ผู้ใช้สามารถเลือกเนื้อหาจากหมวดหมู่ที่ผู้ใช้ต้องการ*



![image](/screen/author.png)
*ผู้ใช้สามารถเลือกเนื้อหาจากผู้เขียนที่ผู้ใช้ต้องการ*

## อ่าน 
![image](/screen/read.png)
*เป็นหน้าหำหรับการอ่านเนื้อหา และทุกครั้งที่มีคนกดเข้าไปยังเนื้อหาก็จะเพิ่มจำนวนผู้อ่านให้กับเนื้อหานั้นๆ*

## แอดมิน
![image](/screen/admin.png)
*เป็นหน้าสำหรับการเขียนบทความ*

# การพัฒนา
## คัดลอกไฟล์ settings.py 
```
COPY settings.py settings_dev.py
```
## คัดลอกไฟล์ manage.py
```
COPY manage.py manage_dev.py
```



## เข้าไปแก้ไขไฟล์ `manage_dev.py` เพื่อให้เรียกใช้ ไฟล์ `settings_dev.py`
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

*เป็นการแยกไฟล์ที่ใช้สำหรับการพัฒนา ออกจากการ Deploy*


# Deployments

## ตั้งค่า wsgi.py
```python
...
...


application = get_wsgi_application()

app = application

```

## ตั้งค่า ALLOW_HOST 

```python 

ALLOWED_HOSTS = [".vercel.app", "127.0.0.1"]

```

## สร้างไฟล์ vercel.json และตั้งค่า

[`vercel.json`](/vercel.json)

```json
{
    "version": 2,
    "builds": [
        {
            "src": "news_writer/wsgi.py",
            "use": "@vercel/python"
        },
        {
            "src": "build_files.sh",
            "use": "@vercel/static-build",
            "config": {
                "distDir": "staticfiles_build"
            }
        }
    ],
    "routes": [
        {
            "src": "/static/(.*)",
            "dest": "/static/$1"
        },
        {
            "src": "/(.*)",
            "dest": "news_writer/wsgi.py"
        }
    ]
    
}

```

