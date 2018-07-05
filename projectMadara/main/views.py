# -*- coding: utf-8 -*-
# from __future__ import unicode_literals


from django.shortcuts import render


from write.models import Toto


# Create your views here.
def about(request):
    context = {}
    template = 'main/about.html'
    return render(request, template, context)


def index(request):
    queryset = Toto.objects.active().order_by("-timestamp")[:10]
    context = {
        "tut_list": queryset,
    }
    template = 'index.html'
    return render(request, template, context)


def explore(request):
    context = {

    }
    template = 'explore.html'
    return render(request, template, context)


def error400(request):
    template = 'errors/400.html'
    context = {}
    return render(request, template, context)


def error403(request):
    template = 'errors/403.html'
    context = {}
    return render(request, template, context)


def error404(request):
    template = 'errors/404.html'
    context = {}
    return render(request, template, context)


def error500(request):
    template = 'errors/500.html'
    context = {}
    return render(request, template, context)


# Google verification
def google_verification(request):
    context = {}
    template = 'google/google5715b52ab8f3659c.html'
    return render(request, template, context)


def partners(request):
    context = {}
    template = 'main/partners.html'

    return render(request, template, context)
