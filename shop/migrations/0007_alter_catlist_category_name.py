# Generated by Django 4.1 on 2022-09-29 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_catlist_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catlist',
            name='category_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
