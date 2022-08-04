# from django.views.generic import TemplateView
from django.views import generic
from .models import Post, Category, Book
from django.shortcuts import render
from .forms import PostForm


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
    queryset = Post.objects.order_by('-created_at').filter(category__pk=category_pk)
    return queryset

class DetailView(generic.DetailView):
  model = Post

def form(request):
  form = PostForm()
  context = {'form': form,}
  return render(request, 'Note/form.html', context)