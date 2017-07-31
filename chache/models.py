from django.db import models

class Chache(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name

class Driver(models.Model):
	name = models.CharField(max_length=50)
	telephone = models.IntegerField()
	def __str__(self):
		return self.name

class Entry(models.Model):
	chache = models.ForeignKey(Chache)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	drivers = models.ManyToManyField(Driver)
	n_comments = models.IntegerField()
	n_pingbacks = models.IntegerField()
	rating = models.IntegerField()

	def __str__(self):
		return self.headline