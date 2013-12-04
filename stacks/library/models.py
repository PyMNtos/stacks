from django.db import models


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

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = 'Book'
		verbose_name_plural = 'Books'

