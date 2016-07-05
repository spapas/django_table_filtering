from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import django_tables2
import books.models
import books.filters
import books.tables


class FilteredSingleTableView(django_tables2.SingleTableView):
    filter_class = None

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter.qs

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


class FilteredTableView(ListView):
    model = books.models.Book

    def get_context_data(self, **kwargs):
        context = super(FilteredTableView, self).get_context_data(**kwargs)
        filter = books.filters.BookFilter(self.request.GET, queryset=self.object_list)
        
        table = books.tables.BookTable(filter.qs)
        django_tables2.RequestConfig(self.request, ).configure(table )

        context['filter'] = filter
        context['table'] = table
        return context
    

class FilteredListView(ListView):
    model = books.models.Book

    def get_context_data(self, **kwargs):
        context = super(FilteredListView, self).get_context_data(**kwargs)
        filter = books.filters.BookFilter(self.request.GET, queryset=self.object_list)
        from django.core.paginator import Paginator
        p = Paginator(filter.qs, 25)
        context['filter'] = filter
        
        return context

