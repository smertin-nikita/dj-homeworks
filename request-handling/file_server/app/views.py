import datetime
import os

from django.shortcuts import render, redirect
from django.urls import reverse

from app import settings


def index(request):
    return redirect(reverse('file_list'))


def file_list(request):
    template_name = 'index.html'

    files = []
    for file_name in os.listdir(settings.FILES_PATH):
        file_path = os.path.join(settings.FILES_PATH, file_name)

        file_info = {
            'name': file_name,
            'ctime': datetime.datetime.fromtimestamp(os.path.getctime(file_path)),
            'mtime': datetime.datetime.fromtimestamp(os.path.getmtime(file_path)),
        }

        files.append(file_info)

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files,
        'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': 'File content!'}
    )

