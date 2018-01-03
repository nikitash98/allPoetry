from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AuthorManager(models.Manager):
    def get_by_natural_key(self, name, pk):
        return self.get(name = name, pk = pk)
class Author(models.Model):
    objects = AuthorManager()
    name = models.CharField(max_length = 100)
    portrait = models.FileField()
    def natural_key(self):
        return(self.name, self.pk)
    def __str__(self):
        return self.name
class Poem(models.Model):
    writer = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.CharField(max_length = 300)
    text = models.TextField()
    keywords = models.TextField()
    def __str__(self):
        return self.title
class Line(models.Model):
    poem = models.ForeignKey(Poem, on_delete = models.CASCADE)
    thewords = models.TextField()
    def __str__(self):
        return self.thewords

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name = "profile")
    picture = models.ImageField(upload_to = 'profiles', blank = True)
    poemfavorites = models.ManyToManyField(Poem, related_name = 'favorited_by')
    linefavorite = models.ManyToManyField(Line, related_name = 'line_favorite')
    def __unicode__(self):
        return self.user.username
