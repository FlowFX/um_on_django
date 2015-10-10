from django.contrib import admin

# import your models here.
from unkenmathe.exercises.models import Exercise

class ExerciseAdmin(admin.ModelAdmin):
	model = Exercise
	list_display = ('id', 'slug', 'content',)

# and register them.
admin.site.register(Exercise, ExerciseAdmin)