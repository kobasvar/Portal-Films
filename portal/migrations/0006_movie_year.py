# Generated by Django 2.2 on 2019-04-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_remove_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(default=None, max_length=4),
        ),
    ]