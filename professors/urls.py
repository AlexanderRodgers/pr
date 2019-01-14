from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.professor_list),
    path('majors/', views.major_list),
    path('majors/<slug:slug>/', views.major_detail)
    # path('', views.index, name='index'),
]