from django.db import models

# Create your models here.
class Exercise(models.Model):
	id = models.AutoField(primary_key=True)
	slug = models.PositiveIntegerField(unique=True)
	content = models.TextField()