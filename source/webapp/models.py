from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from webapp.validate import at_least_8


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тег')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Контент",
                               validators=(at_least_8,))
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='articles',
                               verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    tags = models.ManyToManyField('webapp.Tag', related_name='articles', blank=True)
    article_like = models.ManyToManyField(get_user_model(), related_name='article_like')

    def get_absolute_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.pk})

    def get_comments_count(self):
        return self.comments.count()

    def get_article_likes_count(self):
        return self.article_like.count()

    def __str__(self):
        return f'{self.pk}. {self.title}'


class Comment(models.Model):
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    article = models.ForeignKey('webapp.Article', on_delete=models.CASCADE, related_name='comments',
                                verbose_name="Статья")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='comments',
                               verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    comment_like = models.ManyToManyField(get_user_model(), related_name='comment_like')

    def get_comment_likes_count(self):
        return self.comment_like.count()

    def __str__(self):
        return f'{self.pk}. {self.text[:20]}'

