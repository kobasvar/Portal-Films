# Generated by Django 2.2 on 2019-04-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20190410_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]