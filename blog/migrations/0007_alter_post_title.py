# Generated by Django 3.2.20 on 2023-08-08 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_userpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Some String', max_length=200, unique=True),
        ),
    ]