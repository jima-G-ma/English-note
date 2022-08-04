from django.urls import path
from . import views

app_name = 'Note'

urlpatterns = [
    path('book/', views.IndexView.as_view(), name='index'),
    path('', views.BookView.as_view(), name='book'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('form/', views.form, name='form'),
]
