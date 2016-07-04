from django.core.management.base import BaseCommand, CommandError
import random, string
from books.models import Book

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('book_number', type=int)
        parser.add_argument('author_number',  type=int)
        parser.add_argument('category_number',  type=int)

    def handle(self, *args, **options):
        book_number = options['book_number']
        author_number = options['author_number']
        category_number = options['category_number']
        
        authors = []
        categories = []
        books = []
        
        self.stdout.write(self.style.NOTICE('Will create {} books with {} different authors and {} different categories!'.format(
            book_number, author_number, category_number
        )))
        
        for i in range(author_number):
            first_name = random.choice(string.ascii_uppercase) + ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            last_name = random.choice(string.ascii_uppercase) +  ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
            author_name = first_name+' '+last_name
            authors.append(author_name)
        
        for i in range(category_number):
            category_name =  ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
            categories.append(category_name)
            
        for i in range(book_number):
            title = random.choice(string.ascii_uppercase) +  ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
            book = Book(title=title, author=random.choice(authors), category=random.choice(categories))
            books.append(book)
            
        Book.objects.bulk_create(books)
            
        self.stdout.write(self.style.SUCCESS('Created {} books!!'.format(
            book_number
        )))
            
        """
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        """