from django.shortcuts import render,HttpResponse,redirect
from .models import ToDo
from .models import Book

# Create your views here.
def homepage(request):
    return render(request,"index.html")
def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"test.html",{"todo_list":todo_list})    
def go(request):
    return HttpResponse("This is my first page")    
def second(request):
    return HttpResponse("Test 2 page")
def third(request):
    return HttpResponse("This page test3")    
def books(request):
     book_list = Book.objects.all()
     return render(request,"books.html",{"book_list":book_list})  
def add_todo(request):
    form = request.POST
    text= form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)  
def delete_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)          
