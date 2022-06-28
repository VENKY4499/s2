from django.contrib import admin
from .models import Creator, Member, Event, Vote

admin.site.site_header = "Night Out admin"

class MemberTabularInline(admin.TabularInline):
    model = Member

class VoteInline(admin.StackedInline):
    model = Vote

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    inlines = [MemberTabularInline]
    list_display = ('name', 'email')
    search_fields = ('name',)
    ordering = ['name']

@admin.register(Member)
class InviteeAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_email', 'creator')
    list_filter = ('creator',)
    search_fields = ('creator', 'member_name')
    ordering = ['member_name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [VoteInline, MemberTabularInline]
    list_display = ('event_name', 'creator')
    search_fields = ('event_name', 'creator')
    ordering = ['event_name']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'creator')
    list_filter = ('event_name', 'creator')
    search_fields = ('event_name', 'creator')
    ordering = ['event_name']
