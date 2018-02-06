# Generated by Django 2.0.2 on 2018-02-06 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0005_instagramuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('f', '팔로잉'), ('b', '차단')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('relations', models.ManyToManyField(related_name='_twitteruser_relations_+', through='many_to_many.Relation', to='many_to_many.TwitterUser')),
            ],
        ),
        migrations.AlterField(
            model_name='instagramuser',
            name='following',
            field=models.ManyToManyField(related_name='get_followers', to='many_to_many.InstagramUser'),
        ),
        migrations.AddField(
            model_name='relation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_by_from_user', to='many_to_many.TwitterUser'),
        ),
        migrations.AddField(
            model_name='relation',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_by_to_user', to='many_to_many.TwitterUser'),
        ),
    ]
