from django.db import models
from django.utils import timezone
import datetime


class Author(models.Model):
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name

    def recent_publications(self):
        return self.Publication_set.filter(pub_date__year=timezone.now().year)


class Publication(models.Model):
    #pub_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_authors = models.ManyToManyField(Author)
    pub_name = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("Publication date")
    pub_hyperlink = models.CharField(max_length=1000)
    pub_articletype = models.CharField(max_length=200)

    def __str__(self):
        return self.pub_name


class Website(models.Model):
    website_name = models.CharField(max_length=200)
    website_link = models.CharField(max_length=400)
    website_author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    website_author_string = models.CharField(max_length=200)
    website_lastcheck = models.DateTimeField("Last Checked Date")
    website_numberhits = models.IntegerField('Number of hits')
    def __str__(self):
        return self.website_name + ' for ' + self.website_author.author_name
    # website_name = 'ResearchGate'
    # website_link = 'https://www.researchgate.net/profile/Armin_Doerry/'
    # website_author = 'Doerry'
