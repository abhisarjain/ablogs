# Generated by Django 3.2.6 on 2022-07-13 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_blog_ipadd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='ipadd',
        ),
        migrations.CreateModel(
            name='ipaddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipadd', models.CharField(max_length=50)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.blog')),
            ],
        ),
    ]
