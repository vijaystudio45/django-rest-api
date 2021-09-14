from django.urls import path
from . import views

urlpatterns = [
	path('student-list/', views.student_list, name="student-list"),
	path('student-create/', views.student_create, name="student-create"),
	path('student-update/', views.student_update, name="student_update"),
	path('student-delete/', views.student_delete, name="student_delete"),
]