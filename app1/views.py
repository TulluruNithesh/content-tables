from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app1.models import *
def display_topic(request):
    #topics=Topic.objects.all()
    #topics=Topic.objects.get(topic_name='VolleyBall')
    topics=Topic.objects.filter(topic_name='VolleyBall')
    return render(request,'display_topic.html',context={'ts':topics})

def display_webpage(request):
    #webpages=webpage.objects.all()
    #webpages=webpage.objects.filter(topic_name='VolleyBall')
    #webpages=webpage.objects.all()[0:1:1]
    #webpages=webpage.objects.all().order_by('name')
    #webpages=webpage.objects.all().order_by('-name')
    #webpages=webpage.objects.all().order_by(Length('name'))
    #webpages=webpage.objects.all().order_by(Length('name').desc())
    #webpages=webpage.objects.exclude(topic_name='cricket')
    #webpages=webpage.objects.filter(name__startswith='f')
    #webpages=webpage.objects.filter(name__startswith='a')
    #webpages=webpage.objects.filter(name__endswith='k')
    #webpages=webpage.objects.filter(name__contains='m')
    #webpages=webpage.objects.filter(name__in=['Amy','Erin'])
    webpages=webpage.objects.filter(name__regex=r'f[a-zA-Z]{6}')
    return render(request,'display_webpage.html',context={'ws':webpages})

def display_Access_Record(request):
    Access_Records=Access_Record.objects.all()
    return render(request,'display_Access_Record.html',context={'ar':Access_Records})