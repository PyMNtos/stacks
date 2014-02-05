from django.contrib import admin

from .models import Book, Author, LibraryUser


class BookAdmin(admin.ModelAdmin):
    """
    Our custom BookAdmin.
    """
    list_display = ('title', 'show_authors', 'show_owner', 'publish_date', 'isbn10')
    search_fields = ['title', 'isbn10', 'authors__lastname']
    list_filter = ('publish_date',)

    ordering = ('title', )

    def show_authors(self, book):
        authors = book.authors.all()
        if authors:
            result = '<ul>'
            for author in authors:
                result += '<li>' + unicode(author) + '</li>'
            result += '</ul>'
        else:
            result = ''
        return result

    show_authors.allow_tags = True
    show_authors.short_description = 'Authors'

    def show_owner(self, book):
        return str(book.owner)

    show_owner.short_description = 'Owner'


# Register your models here:
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(LibraryUser)

