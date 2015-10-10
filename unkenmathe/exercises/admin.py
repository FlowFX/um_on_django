from django.contrib import admin

# import your models here.
from unkenmathe.exercises.models import Exercise,Solution

class ExerciseAdmin(admin.ModelAdmin):
	model = Exercise
	list_display = ('id', 'slug', 'content', 'created',)

class SolutionAdmin(admin.ModelAdmin):
	model = Solution
	list_display = ('exercise', 'content',)
	readonly_fields = ('exercise',)


# and register them.
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Solution, SolutionAdmin)