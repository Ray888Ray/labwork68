from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from accounts.models import Profile
from webapp.forms import CommentForm
from webapp.models import Comment, Article


class ArticleCommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comment/create.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        form.instance.article = article
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comment/update.html'
    form_class = CommentForm
    context_object_name = 'comment'

    def has_permission(self):
        return self.request.user.has_perm('webapp.change_comment') or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_comment') or self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk })


class CommentLike(View):

    def get(self, request, *args, **kwargs):

        user = request.user
        post_id = kwargs['pk']
        post_obj = Comment.objects.get(id=post_id)

        if user in post_obj.comment_like.all():
            post_obj.comment_like.remove(user)
        else:
            post_obj.comment_like.add(user)

        return JsonResponse({'key': post_obj.get_comment_likes_count()})




