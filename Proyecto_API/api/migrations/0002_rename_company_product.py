# Generated by Django 4.2.5 on 2023-09-21 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Product',
        ),
    ]