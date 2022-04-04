from django.contrib import admin
from .models import Category, AdPost, AdPostImage

# Register your models here.
admin.site.register(Category)


class AdPostImageInline(admin.StackedInline):
    model = AdPostImage
    fields = ('image',)
    extra = 1
    classes = ['collapse',]

@admin.register(AdPost)
class AdPostAdmin(admin.ModelAdmin):
    inlines = [AdPostImageInline,]

