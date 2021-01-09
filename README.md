# Django Todo Apps
# install
- ikke gjøre å sende filene til github
<br>

- .gitignore
    - tenv er i gitignore
- py -m venv tenv
- .\tenv\Scripts\activate
- pip install django

- pip freeze // det kan være sjekke
- pip freeze >.\requirement.txt    (update)

- django-admin startproject todo_proj (prosjectsnavn)
- settings/SECRET_KEY -> .env
- mv .\todo_proj\ src 

- py -m pip install python-decouple  // .env içine verileri koymamızı sağlıyor
- pip freeze >.\requirement.txt    (update)
<br>

- kan gjøre å sende filene til github
<br>

- py manage.py startapp todo
    - todo/urls.py dosyası oluşturduk  // url yapısını oluşturmak için
    - settings.py içine 'todo' veya 'todo.apps.TodoConfig' ekle 
- py manage.py runserver
<br>

- py manage.py migrate  // Modelde değişiklik yapacaksak migrate komutunu kullanıyoruz
- py manage.py makemigrations
- py manage.py migrate

<br>

- py manage.py createsuperuser

- py manage.py shell
- from fscohort.models import Student
- s1 = Student(first_name="John", last_name="D", number=123)
- s1.save()
- s3 = Student.objects.create(first_name="Mert", last_name="M", number=753) // save e gerek yok
#
// django
/*/*/*/*/*/*/*/*/*/*/
CREATE PROJECT & APP
/*/*/*/*/*/*/*/*/*/*/
$ python -m pip install --upgrade pip
$ py -m venv env
$ .\env\Scripts\activate
$ pip install django
$ pip freeze
$ pip freeze > requirement.txt
$ django-admin startproject clarusway
$ cd clarusway
$ py manage.py startapp fscohort
$ py manage.py runserver // server ı çalıştırma // sonuna çalışmasını istediğimiz portu yazabiliyoruz
$ py manage.py migrate
$ py manage.py createsuperuser
$ py manage.py check // ile hataları da kontrol edebiliriz
https://docs.djangoproject.com/en/3.1/topics/db/models/

/*/*/*/*/*/*/*/*/
M O D E L
/*/*/*/*/*/*/*/*/
fscohort/models.py
from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
MODEL oluşturduktan sonra
$ py manage.py makemigrations  // birleştirmeye hazırlama
$ py manage.py migrate  // birleştirme
$ py manage.py runserver  // serverı tekrar çalıştırıyoruz

// Modelimizi admin.py içeririsine import ediyoruz
from .models import Student
admin.site.register(Student)

Veritabanında veriler obje olarak gözükür. Aşağıdaki şekilde isimler gözükecek
def __str__(self):
        return self.first_name