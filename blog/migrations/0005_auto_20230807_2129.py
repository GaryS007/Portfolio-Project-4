# Generated by Django 3.2.20 on 2023-08-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230807_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
