# Generated by Django 4.1 on 2022-10-13 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_rename_contactus_form_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='text',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='contact_no',
            new_name='phone_no',
        ),
    ]