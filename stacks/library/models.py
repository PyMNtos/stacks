from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class LibraryUser(models.Model):
    user = models.OneToOneField(User)

    # Link to photo probably gravatar
    photo = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return '%s, %s' % (self.user.last_name, self.user.first_name)


class Author(models.Model):
    uuid = models.CharField(max_length=36, default=None, null=False,
                            db_index=True)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    def __unicode__(self):
        return '{0}, {1}'.format(self.lastname, self.firstname)


class Book(models.Model):
    uuid = models.CharField(max_length=36, default=None, null=False,
                            db_index=True)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    authors = models.ManyToManyField(Author)
    publish_date = models.DateField(null=True)
    isbn10 = models.CharField(max_length=10, null=True)
    isbn13 = models.CharField(max_length=13, null=True)
    publisher = models.CharField(max_length=100, null=True)
    thumb = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(LibraryUser, related_name="loaned_books")
    borrower = models.ForeignKey(LibraryUser)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
