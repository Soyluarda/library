from django.shortcuts import render,redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import BookSerializer
from .forms import BookForm
from django.core.files.storage import FileSystemStorage

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


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"



def book_new(request):
    if request.method == "POST":
        book = Book.objects.create()
        book.name = request.POST['name']
        book.book_pic = request.FILES['book_pic']
        book.summary = request.POST['summary']
        book.type = request.POST['type']
        book.save()
        return redirect('all_books')
    else:
        form = BookForm(request.POST or None, request.FILES or None)
    return render(request, 'book_add.html', {'form': form})


def book_update(request,pk):
    books = Book.objects.prefetch_related('author').filter(id=pk)
    if request.method == "POST":
        print(request.FILES['book_pic'],"****")
        for book in books:
            book.name = request.POST['name']
            book.book_pic = request.FILES['book_pic']
            book.summary = request.POST['summary']
            book.type = request.POST['type']
            book.save()
        return redirect('all_books')
    else:
        form = BookForm(request.POST or None, request.FILES or None)
    return render(request, 'book_update.html', {'form': form, 'books':books})


def book_delete(request,id):
    book = Book.objects.filter(id=id)
    book.delete()
    return redirect('all_books')
