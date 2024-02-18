from django.shortcuts import render

# Create your views here.


#def example_view(request):
 #   return render(request, 'bookmodule/example.html')

#def example_view(request):
 #   return render(request, 'includes/header.html')

def header(request):
    return render(request, 'includes/header.html')

