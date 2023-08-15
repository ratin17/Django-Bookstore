from django.urls import path
from book.views import storeBook,showBooks,home

urlpatterns = [
    path('',home,name="home_page"),
    path('storebook/',storeBook,name="storebook"),
    path('showbooks/',showBooks,name="showbooks"),
]