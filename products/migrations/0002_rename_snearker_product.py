# Generated by Django 5.1.3 on 2024-11-24 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snearker',
            new_name='Product',
        ),
    ]
