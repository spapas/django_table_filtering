from django.db.models import Q
import django_filters
import books.models

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = books.models.Book

        
class BookFilterEx(django_filters.FilterSet):
    ex = django_filters.MethodFilter()
    search_fields = ['title', 'author', 'category', 'id', ]

    def filter_ex(self, qs, value):
        if value:
            q_parts = value.split()

            import itertools
            list1=self.search_fields
            list2=q_parts
            perms = [zip(x,list2) for x in itertools.permutations(list1,len(list2))]

            q_totals = Q()
            for perm in perms:
                q_part = Q()
                for p in perm:
                    q_part = q_part & Q(**{p[0]+'__icontains': p[1]})
                q_totals = q_totals | q_part

            qs = qs.filter(q_totals)
        return qs
        
    class Meta:
        model = books.models.Book
        fields = ['ex']