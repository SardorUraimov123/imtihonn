from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    def __str__(self):
        return self.title
    
    
class AboutUs(models.Model):
    body = models.TextField()
    def __str__(self):
        return self.body

class Service(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.FileField(upload_to='service/')
    

class Guards(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
  

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()

    
