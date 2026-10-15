from django.urls import path
from . import views

urlpatterns=[
    path('',views.books_list,name='books_list'),
    path('create/',views.books_create,name='books_create'),
    path('update/<int:id>/',views.books_update,name='books_update'),
    path('delete/<int:id>/',views.books_delete,name='books_delete'),
]