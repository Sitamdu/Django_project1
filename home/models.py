from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank = True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Information(models.Model):
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.address1

class Service(models.Model):
    title = models.CharField(max_length=200)
    logo = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Blogsingle(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Element(models.Model):
    number = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    visit = models.CharField(max_length=200)

    def __str__(self):
        return self.country

class Feedback(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=400)
    image = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email







