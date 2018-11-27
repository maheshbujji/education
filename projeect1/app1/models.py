from django.db import models
class Student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(primary_key=True)
    cno=models.IntegerField()
    clas=models.CharField(max_length=150)
    uname=models.CharField(max_length=150)
    upass=models.IntegerField()
    gender=models.CharField(max_length=10)


class Faculty(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(primary_key=True)
    cno=models.IntegerField()
    subject=models.CharField(max_length=150)
    clas=models.CharField(max_length=150)
    uname=models.CharField(max_length=150)
    upass=models.IntegerField()
    gender=models.CharField(max_length=10)



class Facultyuploading(models.Model):
    Title1=models.CharField(max_length=50)
    Title2=models.CharField(max_length=50)
    clas=models.CharField(max_length=150)
    file=models.FileField()
class BookInfo(models.Model):
    Bookname = models.CharField(max_length=200)
    BookNo = models.IntegerField()
    file = models.CharField(max_length=500)


class Attedence(models.Model):
    name=models.CharField(max_length=150)
    jan=models.IntegerField()
    feb=models.IntegerField()
    mar=models.IntegerField()
    apr=models.IntegerField()
    may=models.IntegerField()
    june=models.IntegerField()
    july=models.IntegerField()
    aug=models.IntegerField()
    sep=models.IntegerField()
    oct=models.IntegerField()
    nov=models.IntegerField()
    dec=models.IntegerField()



