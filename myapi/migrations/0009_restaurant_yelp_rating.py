# Generated by Django 3.0 on 2019-12-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_auto_20191218_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='yelp_rating',
            field=models.FloatField(default=0),
        ),
    ]