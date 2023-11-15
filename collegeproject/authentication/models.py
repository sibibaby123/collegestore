from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class UserExtra(models.Model):
    user = models.ForeignKey(to=User, on_delete = models.CASCADE)
    age=models.IntegerField()
    dateofbirth=models.DateField()
    gender=models.BooleanField(default=True)
    address=models.TextField(max_length=250)
    phonenumber=models.CharField(max_length=20,unique=True)

class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='department',unique=True)
    email=models.EmailField()

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return '{}'.format(self.name)

class Purpose(models.Model):
    name=models.CharField(max_length=20,null=True)
    slug=models.SlugField(max_length=20,unique=True)
    desc=models.TextField(blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    user=models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True,default=None)
    item_pen_no = models.IntegerField(null=True)
    item_book_no = models.IntegerField(null=True)
    item_paper_no = models.IntegerField(null=True)
    booktitle = models.CharField(max_length = 20,null = True)
    bookauthor = models.CharField(max_length = 20,null = True)
    checkedin = models.DateField(null = True)
    class Meta:
        ordering= ('name',)
        verbose_name='purpose'
        verbose_name_plural='purposes'


    def __str__(self):
        return '{}'.format(self.name)

class Collegepart(models.Model):
    name=models.CharField(max_length=20,unique=True)
    slug=models.SlugField(max_length=20,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='collegepart')
    email=models.EmailField()

    class Meta:
        ordering=('name',)
        verbose_name='collegepart'
        verbose_name_plural='collegeparts'

    def __str__(self):
        return '{}'.format(self.name)
class CollegepartImage(models.Model):
    id=models.IntegerField(primary_key=True)
    collegepart = models.ForeignKey(Collegepart,default=None,on_delete=models.CASCADE)
    Image= models.ImageField(upload_to='collegepart')

    def __str__(self):
        return '{}'.format(self.id)
