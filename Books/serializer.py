from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ["book_name", "pub_date", "total_pages", "read_pages", "done_read"]