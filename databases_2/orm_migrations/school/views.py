from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


class StudentsListView(ListView):
    template_name = 'school/students_list.html'
    model = Student
    ordering = 'group'
    queryset = Student.objects.all().prefetch_related('teachers')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def students_list(request):
    template = 'school/students_list.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    context['object_list'] = Student.objects.all().order_by(ordering).prefetch_related('teachers')

    return render(request, template, context)
