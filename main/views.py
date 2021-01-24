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
def openbook(request,id):
     book = Book.objects.get(id=id)
     return render(request,"books_detail.html",{"book_obj":book})       
def add_todo(request):
    form = request.POST
    text= form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)  

def add_book(request):
    form = request.POST
    book = Book(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=form["genre"],
        author=form["author"],
        year=form["year"],
    )
    book.save()
    return redirect(books)  
    
def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)       

def delete_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)      
def mark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=True
    todo.save()
    return redirect(test)    
def unmark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=False
    todo.save()
    return redirect(test)                
    
        
