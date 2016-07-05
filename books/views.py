from django.shortcuts import render
from django.views.generic import TemplateView
import django_tables2
import books.models
import books.filters
import books.tables


class FilteredSingleTableView(django_tables2.SingleTableView):
    filter_class = None

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        return context


class BookFilteredSingleTableView(FilteredSingleTableView):
    model = books.models.Book
    table_class = books.tables.BookTable
    filter_class = books.filters.BookFilter
    
    
class BookSingleTableView(django_tables2.SingleTableView):
    model = books.models.Book
    table_class = books.tables.BookTable
