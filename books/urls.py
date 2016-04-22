from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from books.views import SimpleBookTableFilterView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='books_home.html'), name='books_home', ),
    url(r'^simple_book_table_filter/$', SimpleBookTableFilterView.as_view(), name='simple_book_table_filter', ),
]
