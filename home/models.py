from django.db import models

# Create your models here.

class Message(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name
    

