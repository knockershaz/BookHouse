from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=150,editable=True)
    desc = RichTextUploadingField()
    image = models.ImageField(upload_to="images",editable=True)
    # class Meta:  
    #     db_table = "books" 
