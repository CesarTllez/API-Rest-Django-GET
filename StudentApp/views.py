from django.views import View
from .models import Student
from django.http import JsonResponse

class StudentView(View):
    def get(self, request):
        studentList = Student.objects.all()
        return JsonResponse(list(studentList.values()), safe=False)