from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return self.url
    
class Bookmark(models.Model):        
    link = models.ForeignKey(Link)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return '%s, %s' % (self.user.username, self.link.url)
                
class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    bookmarks = models.ManyToManyField(Bookmark)

    def __unicode__(self):
        return self.name
