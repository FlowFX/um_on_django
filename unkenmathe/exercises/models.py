# exercises/models.py
from django.db import models

from unkenmathe.core.models import TimeStampedModel

# Create your models here.
class Exercise(TimeStampedModel):
	"""
	The class model for exercises.
	"""
	id = models.AutoField(primary_key=True)
	slug = models.PositiveIntegerField(unique=True)
	content = models.TextField()

	def __str__(self):
		return str(self.slug)

class Solution(TimeStampedModel):
	"""
	The class model for solutions.
	Each solution corresponds to exactly one exercise.
	"""
	exercise = models.OneToOneField(Exercise, primary_key=True)
	content = models.TextField()

	def __str__(self):
		return str(self.exercise.slug)