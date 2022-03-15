from django.urls import path
from StudentApp.views import StudentView

urlpatterns = [
    path('student/', StudentView.as_view(), name='student_list')
]