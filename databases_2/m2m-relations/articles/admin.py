from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTag, Tag

admin.site.register(Tag)


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        major_exist = 0
        for form in self.forms:
            if form.cleaned_data.get('major', False):
                major_exist += 1

            if major_exist > 1:
                raise ValidationError('Основным может быть только один раздел')

        if major_exist == 0:
            raise ValidationError('Укажите основной раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]
