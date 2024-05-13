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




#########
def generate_books(request):
    # إنشاء سجلات كتب
    books_data = [
        {"title": "Introduction to Python", "author": "John Smith", "publish_date": date(2020, 1, 15)},
        {"title": "Django for Beginners", "author": "Jane Doe", "publish_date": date(2019, 8, 20)},
        {"title": "Data Science Handbook", "author": "Adam Johnson", "publish_date": date(2021, 5, 10)},
        {"title": "Machine Learning Essentials", "author": "Emily Brown", "publish_date": date(2022, 3, 5)},
        {"title": "Web Development with Django", "author": "Michael Johnson", "publish_date": date(2020, 11, 28)},
        {"title": "Data Structures and Algorithms", "author": "David Lee", "publish_date": date(2018, 6, 12)},
        {"title": "The Art of Programming", "author": "Sophia Martinez", "publish_date": date(2023, 9, 18)},
        {"title": "Python Cookbook", "author": "Matthew Johnson", "publish_date": date(2021, 12, 30)},
        {"title": "Deep Learning Fundamentals", "author": "Ethan Wilson", "publish_date": date(2019, 7, 8)}
    ]

    # إنشاء السجلات
    for book_data in books_data:
        Book.objects.create(**book_data)

    return render(request, 'books_generated.html')
####
from django.shortcuts import render
from .models import Book

def search_books(request):
    query = request.GET.get('query')  # استخراج معايير البحث من الطلب
    
    if query:
        # إجراء البحث بناء على معايير البحث
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()  # عرض جميع الكتب في حالة عدم تقديم معايير البحث
    
    return render(request, 'search_results.html', {'books': books, 'query': query})
#######
from django.shortcuts import render
from .models import Book

def display_books(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})

