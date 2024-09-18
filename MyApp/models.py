from django.db import models
class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  
    published_at = models.DateTimeField()
    url = models.URLField()
    category = models.CharField(max_length=50, default='general')
    country = models.CharField(max_length=50, default='us')

    def __str__(self):
        return self.title

