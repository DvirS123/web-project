from django.db import models

class Job(models.Model):
	'''
	models.Model , saves to data base
	class to introduce new jobs
	show image
	'''
	image = models.ImageField(upload_to ='images/')
	summary = models.CharField(max_length = 100)