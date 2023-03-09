from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=150,editable=True)
    desc = RichTextUploadingField()
    image = models.ImageField(upload_to="images",editable=True)
    cart=models.ManyToManyField(User,related_name='cart',blank=True)
class Order(models.Model):
    title = models.CharField(max_length=150,editable=True)
    cost = models.CharField(max_length=5,editable=True)

def __str__(self):
       return self.title
def get_absolute_url(self):   
   return reverse('post_detail', args=[str(self.id)])
