from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class BookListView(APIView):
    # Get list book
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookDetailView(APIView):
    # Get detail book
    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    