# Generated by Django 3.2.6 on 2023-04-24 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='confirmpassword',
            new_name='name',
        ),
    ]
