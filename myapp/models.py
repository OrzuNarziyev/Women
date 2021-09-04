from django.db import models

# Create your models here.
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat_id = models.ForeignKey('Categories',on_delete=models.CASCADE,blank=True,null=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'post_id':self.pk})

    class Meta:
        verbose_name = 'Women'
        verbose_name_plural = 'Women'


class Categories(models.Model):
    name = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.name