# Generated by Django 3.2.9 on 2022-02-03 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0009_characters'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Characters',
            new_name='Character',
        ),
    ]
