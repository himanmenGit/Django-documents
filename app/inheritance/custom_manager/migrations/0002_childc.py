# Generated by Django 2.0.2 on 2018-02-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
