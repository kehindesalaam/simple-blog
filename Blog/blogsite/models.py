from django.db import models
from django.contrib import admin


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    #imag = models.ImageField(upload_to='/img')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return '/blog/%i' % self.id
        #return reverse(viewname='blogsite.views.Post', args=[str(self.id)])
    
    def __str__(self):
        return self.title


    class Meta:
        ordering = ('-timestamp',)

class Comment(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField(max_length=150)
    post = models.ForeignKey(BlogPost)

    def __str__(self):
        return 'comment by - %s' % self.name

