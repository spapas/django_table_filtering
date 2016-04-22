import django_filters
import books.models

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = books.models.Book