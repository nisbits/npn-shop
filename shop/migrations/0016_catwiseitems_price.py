# Generated by Django 4.1 on 2022-10-14 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_rename_text_contactus_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catwiseitems',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
