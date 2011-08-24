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
            confirm_num = generate_confirm_num()
            save_user(form, confirm_num)
            return redirect(gen_url(form, confirm_num))
    else:
        form = UserForm()
    return render_to_response('add.html', {
        'form': form,
        'csrf_token': csrf(request)['csrf_token']
    })


def gen_url(form, confirm_num):
    """ Generate a reddit compose URL from a form object """
    username = form.cleaned_data['username']
    year = form.cleaned_data['year']
    major = form.cleaned_data['major']
    msg = "Send this message to confirm your /r/CalPoly flair.\n"
    msg += "Confirmation number: " + str(confirm_num)
    args = (("to", "rCalPolyBot"), ("subject", "Add flair"), ("message", msg))
    compose = 'http://reddit.com/message/compose/?'
    return compose + urlencode(args)


def save_user(form, confirm_num):
    """ Given a form object, extract and save the user in the database """
    user = form.save(commit=False)
    user.confirmed = False
    user.confirm_num = confirm_num
    user.save()


def generate_confirm_num():
    """ Generates an integer for use as a confirmation number """
    return int(random() * 10 ** 9)
