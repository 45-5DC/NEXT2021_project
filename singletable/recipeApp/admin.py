from django.contrib import admin
from .models import RecipePost, RecipeComment, RecipeImages

# Register your models here.
admin.site.register(RecipePost)
admin.site.register(RecipeComment)
admin.site.register(RecipeImages)