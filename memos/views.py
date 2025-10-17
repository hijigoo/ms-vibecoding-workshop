from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Memo
from .forms import MemoForm


class MemoListView(LoginRequiredMixin, ListView):
    model = Memo
    template_name = 'memos/memo_list.html'

    def get_queryset(self):
        return Memo.objects.filter(author=self.request.user).order_by('-created_at')


class MemoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Memo
    template_name = 'memos/memo_detail.html'

    def test_func(self):
        memo = self.get_object()
        return memo.is_public or memo.author == self.request.user


class MemoCreateView(LoginRequiredMixin, CreateView):
    model = Memo
    form_class = MemoForm
    template_name = 'memos/memo_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MemoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Memo
    form_class = MemoForm
    template_name = 'memos/memo_form.html'

    def test_func(self):
        memo = self.get_object()
        return memo.author == self.request.user


class MemoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Memo
    template_name = 'memos/memo_confirm_delete.html'
    success_url = reverse_lazy('memos:memo_list')

    def test_func(self):
        memo = self.get_object()
        return memo.author == self.request.user
