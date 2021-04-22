from django.contrib import admin

from .models import Student, Teacher


class TeacherStudentInline(admin.TabularInline):
    model = Student.teachers.through


class StudentTeacherInline(admin.TabularInline):
    model = Teacher.students.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentTeacherInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeacherStudentInline]
