from django.shortcuts import render,redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import BookSerializer


class BookList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        book = Book.objects.select_related('author').all()
        return Response({'books': book})


class BookGetView(RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book.html'
    lookup_fields = ["pk",]

    def get(self,request,pk):
        book = Book.objects.select_related('author', 'publisher').filter(id=pk)
        return render(request, 'book.html', {'books': book})



class AuthorGetView(RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'author.html'
    lookup_fields = ["pk",]

    def get(self,request,pk):
        author = Author.objects.prefetch_related('books').filter(id=pk)
        return render(request, 'author.html', {'authors': author})


class ReadingList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Book.objects.prefetch_related('author').filter(is_read=False)
        return Response({'books': queryset})


class FinishedBooks(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        queryset = Book.objects.prefetch_related('author').filter(is_read=True)
        return Response({'books': queryset})


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


def book_delete(request,id):
    book = Book.objects.filter(id=id)
    book.delete()
    return redirect('all_books')
