from django.db import models

# Create your models here.

class Listings(models.Model):
    listing_url = models.TextField(null=True, blank=True)
    scrape_id = models.TextField(null=True, blank=True)
    last_scraped = models.TextField(null=True, blank=True)
    picture_url = models.TextField(null=True, blank=True)
    host_id = models.TextField(null=True, blank=True)
    host_url = models.TextField(null=True, blank=True)
    host_name = models.TextField(null=True, blank=True)
    host_since = models.TextField(null=True, blank=True)
    host_location = models.TextField(null=True, blank=True)
    host_about = models.TextField(null=True, blank=True)
    host_reponse_time = models.TextField(null=True, blank=True)
    host_response_rate = models.TextField(null=True, blank=True)
    host_is_superhost = models.TextField(null=True, blank=True)
    host_neightbourhood = models.TextField(null=True, blank=True)
    host_listings_count = models.TextField(null=True, blank=True)
    host_total_listings_count = models.TextField(null=True, blank=True)
    neighbourhood = models.TextField(null=True, blank=True)
    neightbourhood_cleansed = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    smart_location =models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)
    property_type = models.TextField(null=True, blank=True)
    room_type = models.TextField(null=True, blank=True)
    accomodates = models.TextField(null=True, blank=True)
    bathrooms =models.TextField(null=True, blank=True)
    bedrooms = models.TextField(null=True, blank=True)
    beds = models.TextField(null=True, blank=True)
    bed_type = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    guests_included = models.TextField(null=True, blank=True)
    extra_people = models.TextField(null=True, blank=True)
    calendar_updated = models.TextField(null=True, blank=True)
    availabilitiy_365 = models.TextField(null=True, blank=True)
    calendar_last_scraped = models.TextField(null=True, blank=True)
    review_scores_rating = models.TextField(null=True, blank=True)
    review_scores_accuracy = models.TextField(null=True, blank=True)
    review_scores_cleanliness = models.TextField(null=True, blank=True)
    review_scores_checkin = models.TextField(null=True, blank=True)
    review_scores_communications = models.TextField(null=True, blank=True)
    review_scores_location = models.TextField(null=True, blank=True)
    review_scores_value = models.TextField(null=True, blank=True)



    class Meta:
        verbose_name_plural = "Listings"



class Reviews(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Reviews"


class Calendars(models.Model):
    date = models.DateField()
    available = models.BooleanField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    adjusted_price = models.TextField(null=True, blank=True)
    minimum_nights = models.IntegerField(null=True, blank=True)
    maximum_nights = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.id

