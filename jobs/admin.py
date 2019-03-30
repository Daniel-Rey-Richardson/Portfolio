#creating new jobs in admin site
#now work with db in visually friendly way

from django.contrib import admin
from .models import Job

# Register your models here.
admin.site.register(Job)