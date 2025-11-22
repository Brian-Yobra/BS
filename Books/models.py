from django.db import models

# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")
    total_pages = models.IntegerField("Page Numbers")
    read_pages = models.IntegerField("No of pages read")
    done_read = models.BooleanField("True or False")
