from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=256)
    qty = models.PositiveIntegerField()

    def __str(self):
        return self.name

