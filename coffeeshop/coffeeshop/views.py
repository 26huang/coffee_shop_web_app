from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm
from django.shortcuts import render

def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))
    # return HttpResponse("hello world!")

def signup(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')

    else:
        form = NameForm()

    template = loader.get_template('signup.html')
    context = {
        'form': form,
    }
    return render(request, 'signup.html', {'form': form})
