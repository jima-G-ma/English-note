from django.urls import path
from . import views

app_name = 'Note'

urlpatterns = [
    path('book/', views.IndexView.as_view(), name='index'),
    path('home/', views.BookView.as_view(), name='book'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('book/form/word/', views.AddPostView.as_view(), name='form_word'),
    path('book/form/<int:pk>', views.AddWordView.as_view(), name='form'),
    path('book/form/book/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>', views.PageView.as_view(), name='page'),
    path('upload/', views.uproad, name='upload'),
    path('note', views.noteView.as_view()),
    path('<int:pk>/update/', views.BookEditView.as_view(), name='editBook'),
    path('<int:pk>/delete/', views.BookDelete.as_view(), name='deleteBook'),
]
