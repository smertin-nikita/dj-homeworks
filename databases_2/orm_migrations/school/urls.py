from django.urls import path

from school.views import students_list, StudentsListView

urlpatterns = [
    path('', StudentsListView.as_view(), name='students'),
    # path('', students_list, name='students'),
]
