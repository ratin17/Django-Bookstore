from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.


def storeBook(request):
    if request.method=="POST":
        book=BookStoreForm(request.POST)
        if book.is_valid():
            book.save(commit=True)
            # print(book.cleaned_data)
            return redirect('showbooks')
    else:
        book=BookStoreForm()
        
    return render(request,'storeBooks.html',{'form':book})

def showBooks(request):
    books=BookStoreModel.objects.all()
    # books=BookStoreModel.objects.get(pk=1)
    # print(books)
    return render(request,'showBooks.html',{'books':books})


def home(request):
    return render(request,'home.html')

def editBook(request,id):
    # print(id)
    book=BookStoreModel.objects.get(pk=id)
    
    if request.method=="POST":
        formData=BookStoreForm(request.POST,instance=book)
        if formData.is_valid():
            formData.save(commit=True)
            # print(formData.cleaned_data)
            return redirect('showbooks')
    else:
        form=BookStoreForm(instance=book)
        return render(request,'storeBooks.html',{'form':form})
    
def deleteBook(request,id):
    BookStoreModel.objects.get(pk=id).delete()
    return redirect('showbooks')