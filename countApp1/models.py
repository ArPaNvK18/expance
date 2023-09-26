from django.db import models

# Create your models here.

class AddAll(models.Model):
    Payment_Type = models.CharField(max_length=200)
    Transaction_Type = models.CharField(max_length=200)
    Rs = models.IntegerField(max_length=200)
    Comment = models.CharField(max_length=400)
    Date = models.DateField()

    def __str__(self):
        return self.Payment_Type

