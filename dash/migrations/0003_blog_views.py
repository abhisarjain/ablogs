# Generated by Django 3.2.3 on 2021-06-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
