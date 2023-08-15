from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.


def storeBook(request):
    if request.method=="POST":
        book=BookStoreForm(request.POST)
        if book.is_valid():
            book.save(commit=True)
            print(book.cleaned_data)
            return redirect('showbooks')
    else:
        book=BookStoreForm()
        
    return render(request,'storeBooks.html',{'form':book})

def showBooks(request):
    books=BookStoreModel.objects.all()
    print(books)
    return render(request,'showBooks.html',{'books':books})


def home(request):
    return render(request,'home.html')