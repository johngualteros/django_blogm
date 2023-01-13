from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from unauthourized.models import Post
from unauthourized.models import Comments
from django.views.generic.detail import DetailView


# Create your views here.

class PostsList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)
        context['count'] = context['posts'].count()

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['posts'] = context['posts'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context


class PostsListAll(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts']

        return context


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'postDetail.html'


class CommentDetail(LoginRequiredMixin, DetailView):
    model = Comments
    context_object_name = 'comments'
    template_name = 'postDetail.html'
