import code
from .models import *
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class AdList(ListView):
    model = Ad
    ordering = '-created_at'
    template_name = 'index.html'
    context_object_name = 'ad'
    paginate_by = 5


class AdDetailView(DetailView):
    model = Ad


class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    fields = ['title', 'content', 'categories', 'image', 'video']
    labels = {
        "title": "Заголовок:",
        "content": "Содержание:",
        "image": "Изображение:",
        "video": "Видео:",
        "categories": "Категория:"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["title"].label = self.labels["title"]
        form.fields["content"].label = self.labels["content"]
        form.fields["categories"].label = self.labels["categories"]
        form.fields["image"].label = self.labels["image"]
        form.fields["video"].label = self.labels["video"]
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    fields = ['title', 'content', 'categories', 'image', 'video']
    labels = {
        "title": "Заголовок:",
        "content": "Содержание:",
        "image": "Изображение:",
        "video": "Видео:",
        "categories": "Категория:"
    }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["title"].label = self.labels["title"]
        form.fields["content"].label = self.labels["content"]
        form.fields["categories"].label = self.labels["categories"]
        form.fields["image"].label = self.labels["image"]
        form.fields["video"].label = self.labels["video"]
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Ad = self.get_object()
        if self.request.user == Ad.author:
            return True
        return False


class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    success_url = '/'

    def test_func(self):
        Ad = self.get_object()
        if self.request.user == Ad.author:
            return True
        return False


# Отправка кода подтверждения на электронную почту.
def generate_random_code():
    pass


def generate_verification_code(self):
    # Код генерируется, сохраняется в поле verification_code и отправляется на e-mail.
    code = generate_random_code()
    self.verification_code = code
    self.save()
    send_mail(
        "Подтверждение регистрации",
        "Код подтверждения: %s" % code,
        "Frostorik@bk.ru",
        [self.email],
        fail_silently=False,
    )
