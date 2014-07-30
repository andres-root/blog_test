from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode


class Category(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	description = models.TextField(blank=True, null=True)
	active = models.BooleanField()
	date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
	date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.name)


class Post(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=255, blank=False, null=False)
	slug = models.CharField(max_length=255, blank=False, null=False)
	content = models.TextField()
	active = models.BooleanField()
	user_create = models.ForeignKey(User)
	date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
	date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.title)