# Generated by Django 3.2.20 on 2023-08-07 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20230807_2129'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPost',
        ),
    ]