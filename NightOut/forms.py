from django import forms
from .models import Creator, Member, Event, Vote


class CreatorForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ('name', 'email')


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('member_name', 'member_email', 'creator', 'event')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('creator', 'event_name')


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('event_name', 'creator', 'event_location1', 'event_location2', 'event_location3',
                  'event_time1', 'event_time2', 'event_time3')
