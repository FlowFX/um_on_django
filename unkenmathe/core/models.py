# core/models.py
from django.db import models


class TimeStampedModel(models.Model):
	"""
	An abstract base class model that provides self-
	updating ``created`` and ``modified`` fields.

	cf. Two Scoops of Django 1.8 p.66
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True