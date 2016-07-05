from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    category = models.CharField(max_length=128)

    def __unicode__(self):
        return '{} by {} ({})'.format(self.title, self.author, self.category)
