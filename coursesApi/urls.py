
from django.urls import path
from .views import (
    CourseListView, 
    CourseDetailView,
    CourseByElectiveView,
    LoadCoursesView,
)

urlpatterns = [
    path('courses', CourseListView, name='course-list'),
    path('courses/<str:course_program>-<str:course_code>', CourseDetailView, name='course-detail'),
    path('courses/', CourseByElectiveView, name='course_by_elective'),
    path('courses/load', LoadCoursesView, name='load-courses'),
    ]
