from django.contrib import admin
from .models import Post, Category, Book
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Book)