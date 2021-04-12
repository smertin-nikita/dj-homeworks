import datetime
import os

from django.shortcuts import render, redirect
from django.urls import reverse

from app import settings


def index(request):
    return redirect(reverse('file_list'))


def file_list(request, date=None):
    template_name = 'index.html'

    files = []
    for file_name in os.listdir(settings.FILES_PATH):
        file_path = os.path.join(settings.FILES_PATH, file_name)

        file_info = {
            'name': file_name,
            'ctime': datetime.datetime.fromtimestamp(os.path.getctime(file_path)),
            'mtime': datetime.datetime.fromtimestamp(os.path.getmtime(file_path)),
        }
        if date:
            if date.date() == file_info['ctime'].date() or date.date() == file_info['mtime'].date():
                files.append(file_info)
        else:
            files.append(file_info)

    context = {
        'files': files,
        'date': date
    }

    return render(request, template_name, context)


def file_content(request, name):
    template_name = 'file_content.html'

    with open(os.path.join(settings.FILES_PATH, name)) as f:
        file_contents = ''.join(f.readlines())

    return render(
        request,
        template_name,
        context={'file_name': name, 'file_content': file_contents}
    )

