# from django.urls import path
from django.views import generic
from .models import Board
from django.urls import reverse_lazy
# from .form import BoardForm


class ListView(generic.ListView):
    template_name = 'board/list.html'
    model = Board
    context_object_name = 'boards'


class DetailView(generic.DetailView):
    template_name = 'board/detail.html'
    model = Board
    context_object_name = 'board'


class CreateView(generic.CreateView):
    template_name = 'board/create.html'
    model = Board
    fields = ('title', 'content', 'author', 'image')
    # form_class = BoardForm
    success_url = reverse_lazy('board:list')


class DeleteView(generic.DeleteView):
    template_name = 'board/delete.html'
    model = Board
    success_url = reverse_lazy('board:list')


class UpdateView(generic.UpdateView):
    template_name = 'board/update.html'
    model = Board
    fields = ('title', 'content', 'author', 'image')
    success_url = reverse_lazy('board:list')
