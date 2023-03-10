# Generated by Django 4.1.2 on 2023-01-30 17:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0018_like_alter_article_options_article_user_article_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user_article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_comment',
        ),
        migrations.AddField(
            model_name='article',
            name='article_like',
            field=models.ManyToManyField(related_name='article_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_like',
            field=models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
