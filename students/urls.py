from django.contrib import admin
from django.urls import path
from students.views import \
    students, \
    students_add, \
    students_edit, \
    contacts

urlpatterns = [
    path('', students, name='students'),
    path('students/', students, name='students'),
    path('students/add/', students_add, name='students-add'),
    path('students/edit/<int:pk>', students_edit, name='students-edit'),
    path('contacts/', contacts, name='students-add'),
]