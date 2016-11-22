from django.db.models import Q
import django_filters
import books.models
import itertools

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = books.models.Book
        exclude = ()

        
class BookFilterEx(django_filters.FilterSet):
    ex = django_filters.CharFilter(label='Ex filter', method='filter_ex')
    search_fields = ['title', 'author', 'category', 'id', ]

    def filter_ex(self, qs, name, value):
        if value:
            q_parts = value.split()
            
            q_totals = Q()
            
            combinatorics = itertools.product([True, False], repeat=len(q_parts) - 1)
            possibilities = []
            for combination in combinatorics:
                i = 0
                one_such_combination = [q_parts[i]]
                for slab in combination:
                    i += 1
                    if not slab: # there is a join
                        one_such_combination[-1] += ' ' + q_parts[i]
                    else:
                        one_such_combination += [q_parts[i]]
                possibilities.append(one_such_combination)

            for p in possibilities:
                list1=self.search_fields
                list2=p
                perms = [zip(x,list2) for x in itertools.permutations(list1,len(list2))]
            
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