from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Author, Website
from datetime import datetime
# Create your views here.


def index(request):
    author_list = Author.objects.order_by('-author_name')
    # hacking, because database backend does not support DISTINCT ON
    website_list = []
    website_names_list = Website.objects.values_list(
        'website_name', flat=True).distinct()
    for website_name in website_names_list:
        website_list.append(Website.objects.filter(
            website_name=website_name)[:1][0])
    # end of hack
    context = {'author_list': author_list,
               'website_list': website_list}
    return render(request, 'webscraper/index2.html', context)


def detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    publications = author.publication_set.all().order_by('-pub_date')
    return render(request, 'webscraper/detail.html', {'author': author, 'publications': publications})


def scrapesite_detail(request, website_id):
    websitelist = Website.objects.filter(
        website_name=Website.objects.get(pk=website_id).website_name)
    return render(request, 'webscraper/scrapesite_detail.html', {'websitelist': websitelist})


# def update(request, author_id):
#     this_author = Author.objects.get(pk=author_id)
#     # Research gate
#     # TODO i want to add a "name" string for each website to author model
#     scrape_list = scrape_researchgate(this_author)
#     npubs = 0
#     for index, row in scrape_list.iterrows():
#         result = this_author.publication_set.filter(
#             pub_name__iexact=row['Name'])
#         if result.count() == 0:
#             npubs += 1
#             this_pub = this_author.publication_set.create(pub_name=row['Name'],
#                                                           pub_date=datetime.strptime(
#                                                               row['Publication Date'], '%b %Y'),
#                                                           pub_hyperlink=row['Hyperlink'],
#                                                           pub_articletype='')
#             # TODO so far, assume single author
#             this_pub.pub_authors.add(Author.objects.get(pk=author_id))
#             this_pub.save()
#     website_rg = this_author.website_set.get(website_name='Research Gate')
#     website_rg.website_numberhits = npubs + website_rg.website_numberhits
#     website_rg.save()
#     # print(scrape_list)
#     return HttpResponseRedirect(reverse('webscraper:detail', args=(author_id,)))
