# from django.views.generic import TemplateView
from django.views import generic
from .models import Post, Category, Book
from django.shortcuts import render
from .forms import PostForm, BookForm, WordForm
from django.urls import reverse_lazy
import csv
from io import TextIOWrapper, StringIO


class IndexView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class BookView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.order_by('-created_at')


class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        queryset = Post.objects.order_by(
            '-created_at').filter(category__pk=category_pk)
        return queryset

class DetailView(generic.DetailView):
    model = Post


class PageView(generic.ListView):
    model = Post
    paginate_by = 10
    template_name = 'paper.html'

    def get_queryset(self):
        book_pk = self.kwargs['pk']
        queryset = Post.objects.order_by(
            '-created_at').filter(book__pk=book_pk)
        return queryset


class AddWordView(generic.CreateView):
    model = Post
    form_class = WordForm
    template_name = 'Note/form.html'
    success_url = reverse_lazy("Note:book")

    def get_initial(self):
        book_pk = self.kwargs['pk']
        initial = super().get_initial()
        initial["book"] = book_pk
        category = Category.objects.get(pk=1)
        initial["category"] = category
        return initial


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Note/form.html'
    success_url = reverse_lazy("Note:book")

    def get_initial(self):
        initial = super().get_initial()
        category = Category.objects.get(pk=1)
        initial["category"] = category
        return initial



class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'Note/book_form.html'
    success_url = reverse_lazy("Note:book")

class BookEditView(generic.UpdateView):
    template_name = 'Note/update.html'
    model = Book
    fields = ('name',)
    success_url = reverse_lazy('Note:book')

class BookDelete(generic.DeleteView):
    # template_name = 'Note/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('Note:book')

def uproad(request):
    if 'csv' in request.FILES:
        # 書き込みモードで開いたファイルオブジェクトはio.TextIOWrapper
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            # postに確認したデータ,createdにデータがあったかどうかが入る
            post, created = Post.objects.get_or_create(question=line[0])
            post.question = line[0]
            post.answer = line[1]
            post.category = Category.objects.get(name=line[2])
            post.book = Book.objects.get(name=line[3])
            post.save()
        return render(request, 'Note/success.html')
    else:
        return render(request, 'Note/upload.html')

class noteView(generic.TemplateView):
    template_name = 'Note/note.html'