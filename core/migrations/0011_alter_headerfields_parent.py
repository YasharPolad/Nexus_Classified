# Generated by Django 4.0.3 on 2022-04-08 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_footerfields_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerfields',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_fields', to='core.headerfields'),
        ),
    ]
