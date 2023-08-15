from django.urls import path
from book.views import storeBook,showBooks,home,editBook,deleteBook

urlpatterns = [
    path('',home,name="home_page"),
    path('storebook/',storeBook,name="storebook"),
    path('showbooks/',showBooks,name="showbooks"),
    path('showbooks/',showBooks,name="showbooks"),
    path('editbook/<int:id>',editBook,name="edit-book"),
    path('deletebook/<int:id>',deleteBook,name="delete-book"),
]