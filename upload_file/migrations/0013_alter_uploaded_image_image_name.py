# Generated by Django 4.1 on 2022-09-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0012_alter_uploaded_image_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaded_image',
            name='image_name',
            field=models.CharField(max_length=40),
        ),
    ]
