# Generated by Django 3.2.3 on 2021-06-10 05:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0005_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='liked',
            field=models.ManyToManyField(null=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
