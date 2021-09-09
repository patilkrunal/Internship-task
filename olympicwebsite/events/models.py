from django.db import models
from django.utils import timezone


class Events(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField(auto_now_add=True)
    event_finish_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.event_name + ' ' + str(self.event_date)

    def event_live(self):
        if self.event_finish_time >= timezone.now():
            return True
        return False


country_list = (
    ('IND', 'India'),
    ('USA', 'USA'),
    ('UK', 'UK')
)


class MedalTally(models.Model):
    medal_type = (
        ('1', 'Gold'),
        ('2', 'Silver'),
        ('3', 'Bronze'),
    )

    medal = models.CharField(max_length=10, choices=medal_type, default='3')
    country = models.CharField(
        max_length=200, choices=country_list, default='1')

    def __str__(self):
        return self.medal + ' ' + self.country


class Cheers(models.Model):
    cheer_count = models.IntegerField(default=0)
    country = models.CharField(
        max_length=200, choices=country_list, default='1')

    def __str__(self):
        return str(self.country) + ' ' + str(self.cheer_count)
