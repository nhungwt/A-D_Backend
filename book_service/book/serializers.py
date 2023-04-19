from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book # this is the model that is being serialized
        fields = "__all__"
        
        