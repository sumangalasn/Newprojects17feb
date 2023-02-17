from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Helloapp


def testing(request):
    mydata = Helloapp.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myhelloapp': mydata,
    }
    return HttpResponse(template.render(context, request))


