# Generated by Django 3.2.4 on 2021-06-26 05:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0004_auto_20210620_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lokes',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
