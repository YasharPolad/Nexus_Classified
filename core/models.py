from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import uuid


# import gettext

class Category(models.Model):
    name = models.CharField(max_length=30)
    order = models.IntegerField(verbose_name="Order in the category filter", 
                            help_text = "The HEAD categories should have the lowest order numbers", unique=True)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, 
                            related_name="subcategories", blank = True, null = True)
    icon = models.CharField(blank = True, null = True, max_length=50)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["-order"]

    def __str__(self):
        if self.parent_category:
            return f"{self.order} {self.parent_category.name} - {self.name}"
        return f"{self.order} {self.name}"
    
    def clean(self):
        if not self.parent_category and not self.icon:
            raise ValidationError({"icon": "All HEAD classes must have icons"})
        super(Category, self).clean()


class AdPost(models.Model):

    ConditionChoices = [
        ("BRN", "Brand New"),
        ("NOB", "New Open Box"),
        ("ULN", "Used - Like New"),
        ("UGC", "Used - Good Condition"),
        ("UPC", "Used - Poor Condition"), 
    ]

    StatusChoices = [
        ("A", "Active"),
        ("S", "Sold"),
        ("E", "Expired"),
        ("F", "Featured"),
        ("P", "Published"),
    ]
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank = True, null = True)
    price = models.FloatField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, related_name="posts", null = True)
    posted_by = models.ForeignKey(get_user_model(), related_name="posts", on_delete = models.CASCADE)
    discount_possible = models.BooleanField(default=True)
    condition = models.CharField(choices = ConditionChoices, max_length = 3)
    brand_name = models.CharField(blank = True, null = True, max_length = 100)
    view_count = models.PositiveIntegerField(blank = True, null = True)
    details = RichTextField(blank = True)
    specifications = models.JSONField(default = list, blank = True)
    status = models.CharField(choices = StatusChoices, max_length = 1)

    def __str__(self):
        return f"{self.name} - {self.status} - {self.price} AZN"

    def save(self, *args, **kwargs):
        if not self.slug:
            to_slug =  str(self.name) + '-' + str(self.posted_by.username) + '-' + str(uuid.uuid4())[:6].replace("-", "")
            self.slug = slugify(to_slug.lower())
        super().save(*args, **kwargs)


class AdPostImage(models.Model):
    image = models.ImageField(upload_to = "adpostimages/")
    adpost = models.ForeignKey("AdPost", on_delete = models.CASCADE, related_name = "adpostimages")

    def __str__(self):
        return self.image.url.replace("/media/adpostimages/", "")


class WebsiteSettings(models.Model):
    logo_header = models.ImageField(upload_to = "logo/", default = "logo.png")
    logo_footer = models.ImageField(upload_to = "logo/", default = "logo.png")
    website_name = models.CharField(max_length = 100)
    phone_main = models.CharField(max_length=20, verbose_name = "Main Phone Number")
    phone_support = models.CharField(max_length=20, verbose_name = "Support Number", blank = True, null = True)
    email_main = models.EmailField(verbose_name = "Main Email Address")
    email_support = models.EmailField(verbose_name = "Support Email Address", null = True, blank = True)
    social_accounts = models.ManyToManyField("SocialAccounts", blank = True)
    about_text = RichTextField(null = True, blank = True)
    address = RichTextField (null = True, blank = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Website Settings"

    def active_social_accounts(self):
        return self.social_accounts.filter(is_active = True)


class SocialAccounts(models.Model):
    name = models.CharField(max_length=30)
    icon_name = models.CharField(max_length=30)
    order = models.PositiveSmallIntegerField()
    link = models.URLField()
    is_active = models.BooleanField(default = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order"] 
        verbose_name_plural = "Social Accounts"  

class HeaderQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active = True)
    
    def footer(self):
        return self.filter(is_active = True, is_footer = True)


class HeaderFields(models.Model):
    name = models.CharField(max_length = 30)
    link = models.URLField()
    order = models.SmallIntegerField()
    parent = models.ForeignKey("self", related_name = "sub_fields", on_delete = models.CASCADE, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_footer = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    items = HeaderQuerySet().as_manager()

    def __str__(self):
        if self.parent:
            return f"{self.order} {self.name} ({self.parent.name})"
        return f"{self.order} {self.name}"          

    class Meta:
        verbose_name_plural = "Header Fields"      


