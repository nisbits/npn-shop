# Generated by Django 4.1 on 2022-09-23 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_catwiseitems_cat_alter_catwiseitems_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catwiseitems',
            name='cat',
            field=models.ForeignKey(choices=[(4, "clothing's"), (1, 'electronics'), (2, 'books'), (7, 'toys'), (6, 'house decoration'), (5, 'kitchen'), (3, 'gaming')], default='1', max_length=100, on_delete=django.db.models.deletion.CASCADE, to='shop.catlist'),
        ),
    ]
