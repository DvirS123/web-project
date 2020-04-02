from django.db import models

class Blog(models.Model):
	'''
	the project will take
	-title-charfield
	-date-datefield
	-body-textfield
	-uploaded-datefield
	-image-imagefield
	'''
	Title = models.CharField(max_length = 100)
	Date = models.DateTimeField()
	Body = models.TextField()
	uploaded = models.DateField(auto_now = False, auto_now_add =True)
	image = models.ImageField(upload_to ='project_images/')


	def modified_date(self):
		return self.Date.strftime('%b / %e / %Y')
