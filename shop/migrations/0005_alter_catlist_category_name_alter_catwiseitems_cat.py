# Generated by Django 4.1 on 2022-09-29 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_catwiseitems_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catlist',
            name='category_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='catwiseitems',
            name='cat',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='shop.catlist'),
        ),
    ]