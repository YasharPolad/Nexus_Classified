# Generated by Django 4.0.3 on 2022-03-31 22:30

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_alter_category_icon_alter_category_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adpost_id', models.SlugField()),
                ('price', models.FloatField()),
                ('discount_possible', models.BooleanField(default=True)),
                ('condition', models.CharField(choices=[('BRN', 'Brand New'), ('NOB', 'New Open Box'), ('ULN', 'Used - Like New'), ('UGC', 'Used - Good Condition'), ('UPC', 'Used - Poor Condition')], max_length=3)),
                ('brand_name', models.CharField(blank=True, max_length=100, null=True)),
                ('view_count', models.PositiveIntegerField()),
                ('details', ckeditor.fields.RichTextField()),
                ('specifications', models.JSONField(default=list)),
                ('status', models.CharField(choices=[('A', 'Active'), ('S', 'Sold'), ('E', 'Expired'), ('F', 'Featured'), ('P', 'Published')], max_length=1)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-order'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='AdPostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='adpostimages/')),
                ('adpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adpostimages', to='core.adpost')),
            ],
        ),
        migrations.AddField(
            model_name='adpost',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='core.category'),
        ),
        migrations.AddField(
            model_name='adpost',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
