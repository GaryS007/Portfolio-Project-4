# Generated by Django 3.2.20 on 2023-08-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_contactenquiry_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactenquiry',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
