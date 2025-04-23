from django.db import models
from django.contrib.auth.models import User

class BookTable(models.Model):
    btitle = models.CharField(max_length=170)
    blogo = models.ImageField(upload_to='booklogos/', blank=True, null=True)
    bauthor = models.CharField(max_length=130)
    bgenre = models.CharField(max_length=42)
    bdescription = models.TextField()
    bk_requesters = models.ManyToManyField(User, related_name='requested_bks', blank=True)

    def __str__(self):
        return self.title