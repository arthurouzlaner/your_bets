# Generated by Django 2.1.5 on 2019-01-29 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='PersonalData',
        ),
    ]