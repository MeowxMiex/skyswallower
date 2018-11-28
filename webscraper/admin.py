from django.contrib import admin

from .models import Author, Publication, Website
# Register your models here.

admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(Website)