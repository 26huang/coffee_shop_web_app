from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    template = loader.get_template('main/home.html')
    context = {}
    return HttpResponse(template.render(context, request))
    # return HttpResponse("hello world!")