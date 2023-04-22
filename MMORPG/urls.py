from django.urls import path
from . import views
from django.contrib import admin
from .views import AdList, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView

urlpatterns = [
    path('', AdList.as_view()),
    path('<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    path('create/', AdCreateView.as_view(), name='ad-create'),
    path('<int:pk>/update/', AdUpdateView.as_view(), name='ad-update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad-delete'),
]
