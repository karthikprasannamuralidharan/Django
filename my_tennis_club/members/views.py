from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

# Create your views here.
def members(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,slug):
    mymembers = Members.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Bananna', 'Cherry'],
        'fruit': ['Apple', 'Bananna', 'Cherry'],
        'mymembers': mymembers,
        'greeting': 1,
        
    }
    return HttpResponse(template.render(context,request))