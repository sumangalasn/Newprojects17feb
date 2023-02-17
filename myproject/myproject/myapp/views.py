from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Myapp


def testing(request):
    mydata = Myapp.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'bymyapp': mydata,
    }
    return HttpResponse(template.render(context, request))
