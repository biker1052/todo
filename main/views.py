from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Hello world")
def test(request):
    return render(request,"test.html")    
def go(request):
    return HttpResponse("This is my first page")    
