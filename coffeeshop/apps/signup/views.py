from django.template import loader
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.shortcuts import render


# Create your views here.
def signup(request):
    form = NameForm()

    if request.method == 'POST':
        print('post true')
        form = NameForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks/')

    else:
        print('post false')

    context = {
        'form': form,
    }
    return render(request, 'signup/signup.html', context)


def thanks(request):
    return render(request, 'signup/thanks.html')