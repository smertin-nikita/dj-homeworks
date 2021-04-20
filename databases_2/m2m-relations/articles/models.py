from django.db import models


class Tag(models.Model):

    title = models.CharField(max_length=256, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    tags = models.ManyToManyRel(
        Tag,
        through='ArticleTag'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    major = models.BooleanField(
        blank=False,
        null=False,
        default=False,
        verbose_name='Основной'
    )
