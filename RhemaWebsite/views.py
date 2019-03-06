from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><head><title>Rhema's Website</title></head><body><center><br/><br/><br/><br/><h1>This is Rhema Mary James Page</h1><br/><br/><br/></center></body></html>")