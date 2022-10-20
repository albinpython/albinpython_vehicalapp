from django.db import models

# Create your models here.
class CRUD(models.Model):

    Vehicle_Number=models.CharField(max_length=20)
    Vehicle_type=models.CharField(max_length=20)
    Vehicle_model=models.CharField(max_length=50)
    Vehicle_description=models.TextField()
