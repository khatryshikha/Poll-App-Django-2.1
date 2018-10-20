from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length = 200)
    public_date = models.DateTimeField('date publish')

class Choices(models.Model):
    question = models.ForeignKey(Questions,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)