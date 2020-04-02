from django.db import models

class Project(models.Model):
	'''
	the blog will take
	-title-charfield
	-date-datefield
	-body-textfield
	-uploaded-datefield
	-image-imagefield
	'''
	Title = models.CharField(max_length = 100)
	Date = models.DateTimeField()
	Description = models.TextField()
	uploaded = models.DateField(auto_now = False, auto_now_add =True)
	image = models.ImageField(upload_to ='projects_images/')
	File = models.FileField(upload_to = 'projects_files/')

	def modified_date(self):
		return self.Date.strftime('%b / %e / %Y')
