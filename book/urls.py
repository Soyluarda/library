from django.urls import path, re_path
from .views import BookList, BookGetView, AuthorGetView, ReadingList, FinishedBooks, BookUpdateAPIView, book_delete, book_new, book_update

urlpatterns = [
    path('', BookList.as_view(),name='all_books'),
    path('book/<int:pk>', BookGetView.as_view(), name='book_get_view'),
    path('book/add/', book_new, name='book_create_view'),
    re_path(r'book/delete/(?P<id>[0-9]+)/', book_delete, name="book_delete_view"),
    path('book/update/<int:pk>', book_update, name="book_update_view"),
    path('author/<int:pk>/', AuthorGetView.as_view(), name='author_get_view'),
    path('reading-list/', ReadingList.as_view(), name='reading_list'),
    path('finished-books/', FinishedBooks.as_view(), name='finished_books'),

]
