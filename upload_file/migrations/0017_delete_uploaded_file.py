# Generated by Django 4.1 on 2022-09-21 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0016_remove_uploaded_image_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='uploaded_file',
        ),
    ]
