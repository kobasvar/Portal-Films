# Generated by Django 2.2 on 2019-04-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20190410_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviereview',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
