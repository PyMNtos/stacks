from django.core.management.base import NoArgsCommand
from django.template import Template, Context
from django.conf import settings
from library.models import Book


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        book = Book.objects.get(uuid="aaa")
        book.delete()
        book = Book.objects.get(uuid="aab")
        book.delete()
        book = Book.objects.get(uuid="aac")
        book.delete()
