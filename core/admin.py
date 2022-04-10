from django.contrib import admin
from .models import Category, AdPost, AdPostImage, HeaderFields, WebsiteSettings, SocialAccounts

# Register your models here.
admin.site.register(HeaderFields)
admin.site.register(WebsiteSettings)
admin.site.register(SocialAccounts)


class AdPostImageInline(admin.StackedInline):
    model = AdPostImage
    fields = ('image',)
    extra = 1
    classes = ['collapse',]

@admin.register(AdPost)
class AdPostAdmin(admin.ModelAdmin):
    inlines = [AdPostImageInline,]

