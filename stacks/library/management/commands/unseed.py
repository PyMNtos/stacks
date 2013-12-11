from django.core.management.base import NoArgsCommand
from django.template import Template, Context
from django.conf import settings
from library.models import Book

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        uuids = ['aaa', 'aab', 'aac']
        for uuid in uuids:
            try:
                book = Book.objects.get(uuid=uuid)
                book.delete()
            except Book.DoesNotExist:
                pass
