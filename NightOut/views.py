from django.shortcuts import render
from .models import *
from .forms import *

now = timezone.now()

def home(request):
    return render(request, 'nightout/home.html')

def login(request):
    return render(request, 'nightout/login.html')

def create_event(request):
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_date = timezone.now()
            event.save()
            events = Event.objects.filter(created_date__lte=timezone.now())
            return render(request, 'nightout/home.html',
                          {'events', events})
    else:
        form = VoteForm()
    return render(request, 'nightout/create_event.html', {'form': form})
