from django.core.management.base import BaseCommand
import csv
import os
from django.conf import settings
from ...models import Reviews, Listings, Calendars
import difflib


class Command(BaseCommand):
    help = 'Add Default Groups'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Indicates name of the file to be inserted into database')


    def _populate_reviews(self, p_name):
        file_path = os.path.join(settings.STATIC_ROOT + "/csv/" + p_name)
        print('Reviews datbase begin: Started !')
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            i=0
            for row in reader:
                    p = Reviews(listing_id=row['listing_id'],
                                date=row['date'])
                    p.save()
                    i=i+1
                    if (i % 100) == 0:
                        print('{} rows inserted...'.format(i))
                    print(i)
            print('Reviews populated...')


    def _populate_listings(self, p_name):
        print('Listings datbase begin: Started !')
        file_path = os.path.join(settings.STATIC_ROOT + "/csv/" + p_name)
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            i=0
            for row in reader:
                p = Listings(id_number = row['id'],
                             name=row['name'],
                             host_id=row['host_id'],
                             host_name=row['host_name'],
                             neighbourhood_group=row['neighbourhood_group'],
                             neighbourhood=row['neighbourhood'],
                             latitude=row['latitude'],
                             longitude=row['longitude'],
                             room_type=row['room_type'],
                             price=row['price'],
                             minimum_nights=row['minimum_nights'],
                             number_of_reviews=row['number_of_reviews'],
                             last_review=row['last_review'],
                             reviews_per_month=row['reviews_per_month'],
                             calculated_host_listings_count=row['calculated_host_listings_count'],
                             availability_365=row['availability_365']
                             )
                p.save()
                i = i + 1
                print('{}'.format(i))
                if (i%100) == 0:
                    print('{} rows inserted...'.format(i))
        print('Listings populated...')


    def _populate_calendars(self, p_name):
        print('Calendar datbase begin: Started !')
        file_path = os.path.join(settings.STATIC_ROOT + "/csv/" + p_name)
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            i=0
            for row in reader:
                p = Calendars(
                    listing_id=row['listing_id'],
                    date=row['date'],
                    available=row['available'],
                    price=row['price'],
                    adjusted_price=row['adjusted_price'],
                    minimum_nights=row['minimum_nights'],
                    maximum_nights=row['maximum_nights']
                )
                p.save()
                i = i + 1
                if (i % 100) == 0:
                    print('{} rows inserted...'.format(i))
            print('Calendar populated...')


    def handle(self, *args, **kwargs):

        for filename in os.listdir(kwargs['name']):

            seq1 = difflib.SequenceMatcher(None, '_populate_listings', filename)
            seq2 = difflib.SequenceMatcher(None, '_populate_reviews', filename)
            seq3 = difflib.SequenceMatcher(None, '_populate_calendars', filename)


            listing = seq1.ratio()
            review = seq2.ratio()
            calendar = seq3.ratio()

            runner = max(listing, calendar, review)

            if runner == listing:
                print('Populating database from listings.csv...')
                self._populate_listings(filename)
                print('Database populated !!')
            elif runner == review:
                print('Populating database from reviews.csv...')
                self._populate_reviews(filename)
                print('Database populated !!')
            elif runner == calendar:
                print('Populating database from calendars.csv...')
                self._populate_calendars(filename)
                print('Database populated !!')
            else:
                print('Something is terribly wrong...')

        print('Finally, Database populate complete !!')




