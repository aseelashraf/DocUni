# Generated by Django 2.2 on 2019-04-22 06:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_comment_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='file_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
