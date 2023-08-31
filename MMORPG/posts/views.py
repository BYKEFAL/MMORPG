from django.shortcuts import render, redirect
from django.urls import reverse_lazy, resolve
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import PostAddForm


class Home(TemplateView):
    template_name = 'homepage/index.html'


class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    ordering = ['id']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postroll'] = Post.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj


class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:posts_page')


class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create_update.html'
    form_class = PostAddForm

    # Переопределяем метод, чтобы публикации создавались только от имени авторизированного
    # пользователя без возможности выбора
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostCreate, self).form_valid(form)

    # def get_initial(self):
    #     return {'author': self.request.user.username}

    # def get_initial(self):
    #     self.initial.update({'author': self.request.user.username})
    #     return super(PostCreate, self).get_initial()


class PostUpdate(UpdateView):
    template_name = 'posts/post_create_update.html'
    form_class = PostAddForm
    # success_url = reverse_lazy('posts:posts_page')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostsProfileList(ListView):
    model = Post
    template_name = 'posts/posts_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user.id)
        return context
