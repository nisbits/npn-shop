# Generated by Django 4.1 on 2022-09-03 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='uploaded_file',
        ),
    ]