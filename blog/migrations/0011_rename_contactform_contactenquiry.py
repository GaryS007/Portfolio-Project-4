# Generated by Django 3.2.20 on 2023-08-10 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20230810_1958'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='ContactEnquiry',
        ),
    ]