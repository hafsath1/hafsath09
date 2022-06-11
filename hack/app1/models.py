from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class registration(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class addbook(models.Model):
    bookid=models.IntegerField()
    bookname=models.CharField(max_length=50)
    bookauthur=models.CharField(max_length=50)
    bookprice=models.IntegerField()

    def __str__(self):
        return self.bookname