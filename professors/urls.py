from django.urls import path
from . import views

urlpatterns = [
    path('professors/', views.professor_list),
    path('professors/<int:pk>/', views.professor_detail_id),
    path('professors/<slug:slug>/', views.professor_detail),
    path('majors/', views.major_list),
    path('majors/<int:pk>/', views.major_detail_pk),
    path('majors/<slug:slug>/', views.major_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:pk>/', views.professor_review)
]