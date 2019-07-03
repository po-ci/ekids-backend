from django.contrib import admin
from .Models import Category, CategoryItem
# Register your models here.

admin.site.register(Category.Category)
admin.site.register(CategoryItem.CategoryItem)
