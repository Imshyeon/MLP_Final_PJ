# Generated by Django 4.2.7 on 2023-12-07 01:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FE', '0016_alter_comment_parentcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]