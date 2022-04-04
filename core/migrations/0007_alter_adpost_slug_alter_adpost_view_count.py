# Generated by Django 4.0.3 on 2022-04-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_adpost_adpost_id_adpost_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adpost',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='adpost',
            name='view_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
