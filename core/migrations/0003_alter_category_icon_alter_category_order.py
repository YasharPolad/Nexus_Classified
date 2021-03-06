# Generated by Django 4.0.3 on 2022-03-31 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(help_text='The HEAD categories should have the lowest order numbers', unique=True, verbose_name='Order in the category filter'),
        ),
    ]
