# Generated by Django 5.1.2 on 2024-10-23 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='evaluation',
            new_name='evaluation_number',
        ),
    ]
