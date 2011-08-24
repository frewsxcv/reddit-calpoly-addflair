from add_flair.forms import UserForm
from add_flair.models import User
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from urllib import urlencode
from random import random


def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            year = form.cleaned_data['year']
            major = form.cleaned_data['major']
            confirm_num = generate_confirm_num()
            message = "Send this message to confirm your /r/CalPoly flair.\n"
            message += "Confirmation number: " + str(confirm_num)
            args = (("to", "rCalPolyBot"), ("subject", "Add flair"),
                    ("message", message))
            compose = 'http://reddit.com/message/compose/?'
            user = form.save(commit=False)
            user.confirmed = False
            user.confirm_num = confirm_num
            user.save()
            return redirect(compose + urlencode(args))
    else:
        form = UserForm()
    return render_to_response('add.html', {
        'form': form,
        'csrf_token': csrf(request)['csrf_token']
    })


def generate_confirm_num():
    """ Generates an integer for use as a confirmation number """
    return int(random() * 10 ** 9)
