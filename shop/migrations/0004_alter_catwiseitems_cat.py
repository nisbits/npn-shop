# Generated by Django 4.1 on 2022-09-29 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_catwiseitems_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catwiseitems',
            name='cat',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='shop.catlist'),
        ),
    ]
