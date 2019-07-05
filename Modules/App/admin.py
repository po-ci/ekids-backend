from django.contrib import admin
from .Models import Category, Vocabulary
# Register your models here.

admin.site.register(Category.Category)
admin.site.register(Vocabulary.Vocabulary)
