from django.http import HttpResponse
from addFlair.forms import RegistrationForm
from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def add(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponse('congrats!')
    else:
        form = RegistrationForm()
    return render_to_response('add.html', {
        'form': form,
        'csrf_token': csrf(request)['csrf_token']
    })
