# in terminal$ python manage.py makemigrations 
# make migrations everytime make a job

# then run$ python manage.py migrate 
# this will make all migrations 
# save things into db through django
from django.db import models

# Create your models here.
class Job(models.Model):
	# Image 
	image = models.ImageField(upload_to='images/')
	# Summary
	summary = models.CharField(max_length=200) # 200 is max length of summary can be more

	#job title in admin
	def __str__(self):
		return self.summary