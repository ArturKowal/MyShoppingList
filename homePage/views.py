from django.shortcuts import render


def index(request):
    template = "index.html"
    context = {}
    return render(request, template, context)


def about(request):
    template = "about.html"
    context = {}
    return render(request, template, context)


def room(request, pin):
    template = "room.html"
    context = {"pin": pin}
    return render(request, template, context)
