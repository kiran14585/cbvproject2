from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Book
from django.urls import reverse_lazy


# Create your views here.
class BookListView(ListView):
    model = Book
    # template_name = 'testapp/books.html'
    # context_object_name = 'books'
    # default template file : book_list.html
    # default context object : book_list


class BookListView2(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    # default template file : book_detail.html
    # default context object : book or object

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    # fields = ('title','author','pages','price')

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

class BookDeleteview(DeleteView):
    model = Book
    success_url = reverse_lazy('listbooks')
