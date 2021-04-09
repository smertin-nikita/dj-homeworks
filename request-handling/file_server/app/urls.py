from django.urls import path, register_converter

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app.converters import DatetimeConverter
from app.views import file_list, file_content

register_converter(DatetimeConverter, 'datetime')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('files/', file_list, name='file_list'),
    path('files/<datetime:date>', file_list, name='file_list'),
    path('files/<filename:name>', file_content, name='file_content'),
]
