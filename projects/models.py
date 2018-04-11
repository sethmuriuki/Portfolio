from django.db import models
import datetime as dt

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length =60)
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to = 'projects/', null = True, blank = True)
    image = models.ImageField(upload_to = 'images/', null = True)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
