from django.urls import path
from .views import ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]
