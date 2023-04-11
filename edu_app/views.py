from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index1.html')

def course(request):
    return render(request,'course.html')

def gallery(request):
    return render(request,'gallery.html')

def placement(request):
    return render(request,'placement.html')

def contact(request):
    return render(request,'contact.html')