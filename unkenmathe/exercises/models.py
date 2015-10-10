# exercises/models.py
from django.db import models

from unkenmathe.core.models import TimeStampedModel

# Create your models here.
class Exercise(TimeStampedModel):
	id = models.AutoField(primary_key=True)
	slug = models.PositiveIntegerField(unique=True)
	content = models.TextField()
