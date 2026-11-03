from django.urls import path
from . import views

urlpatterns=[
    path('', views.course_list_view, name='display_courses'),
    path('course-detail/<str:course_code>/', views.course_details_view, name='details'),
]