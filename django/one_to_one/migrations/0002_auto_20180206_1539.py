# Generated by Django 2.0.2 on 2018-02-06 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one_to_one', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='serves_hot_dog',
            new_name='serves_hot_dogs',
        ),
    ]
