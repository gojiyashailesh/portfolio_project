

# Create your views here.
# portfolio/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')
