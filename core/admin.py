from django.contrib import admin
from .models import Category, AdPost, AdPostImage

# Register your models here.
admin.site.register(Category)
admin.site.register(AdPost)
admin.site.register(AdPostImage)

