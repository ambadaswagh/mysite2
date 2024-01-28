
from django import http
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext  as _

def index(request):
    output = _('WelcomeHeading')
    context ={'temp':'Test 1'}
    return render(request,'languageSelection/index.html', context)
