# Generated by Django 2.2 on 2019-05-12 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='photos/user-profile.png', upload_to='users/%Y/%m/%d/'),
        ),
    ]