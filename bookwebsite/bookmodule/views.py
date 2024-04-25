from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homepage(request):
  return HttpResponse('hello world')
#def example_view(request):
 #   return render(request, 'bookmodule/example.html')

#def example_view(request):
 #   return render(request, 'includes/header.html')

def header(request):
    return render(request, 'includes/header.html')

def listbooks(request):
    return render(request,'includes\listbooks.html')

def model(request):
    return render(request,'includes\model.html')
def books(request):
    return render(request,'includes\books.html')

def we(request):
    return render(request,'includes\we.html')
