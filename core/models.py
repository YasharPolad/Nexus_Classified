from distutils.command.upload import upload
from django.db import models
from django.core.exceptions import ValidationError

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