# Generated by Django 4.1 on 2022-10-04 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_catlist_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='catwiseitems',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]