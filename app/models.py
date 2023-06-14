from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()
    image_url = models.URLField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text[:80]


