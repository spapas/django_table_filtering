"""django_table_filtering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from books.views import BookFilteredSingleTableView, BookSingleTableView, FilteredTableView, FilteredListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', BookFilteredSingleTableView.as_view() ),
    url(r'^nofilter/$', BookSingleTableView.as_view() ),
    url(r'^notable/$', FilteredListView.as_view() ),
    url(r'^filter2/$', FilteredTableView.as_view() ),
]
