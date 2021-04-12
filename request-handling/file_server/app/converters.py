import os
from datetime import datetime

from django.urls.converters import StringConverter

from app import settings


class DatetimeConverter:
    regex = r'[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self.format)

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)


class FilenameConverter(StringConverter):

    # если знаем что все файлы называются server.[0-9]{2} можно сделать регулярку
    # regex = r'server\.[0-9]{2}'

    def to_python(self, value: str) -> str:
        if os.path.exists(os.path.join(settings.FILES_PATH, value)):
            return value
        else:
            raise ValueError("File doesn't exist")

    def to_url(self, value: str) -> str:
        return value
