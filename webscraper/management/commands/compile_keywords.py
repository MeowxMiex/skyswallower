from django.core.management.base import BaseCommand, CommandError
from webscraper.models import Publication
from webscraper.scrape_function.scrape_researchgate_module import scrape_researchgate
from datetime import datetime
from webscraper.management.commands.rake_nltk import Metric, Rake
from webscraper.management.commands.summa import keywords


class Command(BaseCommand):
    help = 'Compiling keyword list'

    def handle(self, *args, **options):

        all_publications = Publication.objects.all()
        abstract_txt = ''
        for pub in all_publications:
            abstract_txt += pub.pub_name

        # stopwords_list = ['using', 'have', 'been', 'via', 'for', 'is', 'the', 'a', 'with', 'new', 'on',
            #   'on', 'of', 'while', 'based', 'in', 'to', 'and', 'are', 'that', 'it', 'can', 'be', 'introduces', 'perform', 'this', 'various']

        # punctuations_list = ['≥', '.', ',', '-', '(', ')']

        # r = Rake(stopwords=stopwords_list, punctuations=punctuations_list)
        r = Rake()
        r.extract_keywords_from_text(abstract_txt)
        # To get keyword phrases ranked highest to lowest.
        print(r.get_ranked_phrases_with_scores())

        # print(keywords.keywords(abstract_txt))
