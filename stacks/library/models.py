from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

<<<<<<< HEAD
@python_2_unicode_compatible
class Book(models.Model):
	uuid = models.CharField(max_length=36, default=None, null=False, db_index=True)
	title = models.CharField(max_length=200, null=False)
	author_lastname = models.CharField(max_length=50)
	author_firstname = models.CharField(max_length=50)
	description = models.TextField(null=True)
	publish_date = models.DateField(null=True)
	isbn10 = models.CharField(max_length=10, null=True)
	isbn13 = models.CharField(max_length=13, null=True)
	publisher = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Book'
		verbose_name_plural = 'Books'
=======
class Author(models.Model):
    uuid = models.CharField(max_length=36, default=None, null=False, db_index=True)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    def __unicode__(self):
        return '{0}, {1}'.format(self.lastname, self.firstname)


class Book(models.Model):
    uuid = models.CharField(max_length=36, default=None, null=False, db_index=True)
    title = models.CharField(max_length=200, null=False)

    authors = models.ManyToManyField(Author)

    description = models.TextField(null=True)
    publish_date = models.DateField(null=True)
    isbn10 = models.CharField(max_length=10, null=True)
    isbn13 = models.CharField(max_length=13, null=True)
    publisher = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


>>>>>>> 0220ac611ebfdf74c61cc1cfa0c9106a6ac950c6

