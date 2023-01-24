from django.db import models

# Create your models here.

class ParseData(models.Model):
    parse_type = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=900, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    published_datetime = models.DateTimeField(blank=True, null=True)
    attachment_list = models.TextField(blank=True, null=True, default="empty")

    def __str__(self):
        return self.title