from django.db import models
from django.utils import timezone

class Creator(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    member_name = models.CharField(max_length=50)
    member_email = models.EmailField(max_length=100)
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE, null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)

class Event(models.Model):
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE, primary_key=True)
    event_name = models.CharField(max_length=50)

    def __str__(self):
        return self.event_name

class Vote(models.Model):
    event_name = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE, null=True)
    event_location1 = models.CharField(max_length=50)
    event_location2 = models.CharField(max_length=50)
    event_location3 = models.CharField(max_length=50)
    event_time1 = models.DateTimeField(default=timezone.now)
    event_time2 = models.DateTimeField(default=timezone.now)
    event_time3 = models.DateTimeField(default=timezone.now)