from datetime import datetime


class DatetimeConverter:
    regex = r'[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format)

    def to_url(self, value):
        return value.strftime(self.format)


class FilenameConverter:
    pass