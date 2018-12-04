from django.core.management.base import BaseCommand, CommandError
from webscraper.models import Author
from webscraper.scrape_function.scrape_researchgate_module import scrape_researchgate
from datetime import datetime


class Command(BaseCommand):
    help = 'Performs scraping to update database'

    def handle(self, *args, **options):
        self.stdout.write('Testing')
        # all_authors = Author.objects.all()
        all_authors = Author.objects.filter(author_name='Moreira')
        for this_author in all_authors:
            npubs = 0
            # TODO i want to add a "name" string for each website to author model
            scrape_list = scrape_researchgate(this_author)
            for index, row in scrape_list.iterrows():
                result = this_author.publication_set.filter(
                    pub_name__iexact=row['Name'])
                print(row['Name'] + ' ' + str(result.count()))
                if result.count() == 0:
                    npubs = npubs + 1
                    this_pub = this_author.publication_set.create(pub_name=row['Name'],
                                                                  pub_date=datetime.strptime(
                                                                      row['Publication Date'], '%b %Y'),
                                                                  pub_hyperlink=row['Hyperlink'],
                                                                  pub_articletype='',
                                                                  pub_abstract=row['Abstract'])
                    # TODO so far, assume single author
                    this_pub.pub_authors.add(this_author)
                    this_pub.save()
                else:
                    if result[0].pub_abstract == '':
                        result_to_write = result[0]
                        result_to_write.pub_abstract = row['Abstract']
                        result_to_write.save()

            website_rg = this_author.website_set.get(
                website_name='Research Gate')
            website_rg.website_numberhits = npubs + website_rg.website_numberhits
            website_rg.save()
