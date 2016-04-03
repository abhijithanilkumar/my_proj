from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

class NCSide(models.Model):
    nc_id = models.IntegerField()
    username = models.CharField(max_length = 15, unique=True)
    password = models.CharField(max_length = 20)
    def __str__(self):              # __unicode__ on Python 2
        return self.username


class Menu(models.Model):
    nc = models.ForeignKey(NCSide)
    item_code = models.IntegerField()
    item_name = models.CharField(max_length = 20)
    price = models.IntegerField()
    upload = models.FileField(upload_to='media/')

    def __str__(self):              # __unicode__ on Python 2
        return self.item_name


class Student(models.Model):
    s_username = models.CharField(max_length = 15, unique=True)
    s_password = models.CharField(max_length = 20)

    def __str__(self):              # __unicode__ on Python 2
        return self.s_username

class Register(models.Model):
    s_user = models.ForeignKey(Student)
    s_name = models.CharField(max_length = 20)
    s_phone = models.IntegerField(validators=[MinValueValidator(7000000000), MaxValueValidator(9999999999)])
    s_block = models.CharField(max_length = 20)

    def __str__(self):              # __unicode__ on Python 2
        return self.s_name


class Order(models.Model):
    s_details = models.ForeignKey(Register)
    order = models.ForeignKey(Menu)
    quantity = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.order
