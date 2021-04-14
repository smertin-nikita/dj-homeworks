from datetime import datetime, timedelta

from django import template


register = template.Library()


@register.filter
def format_date(value):
    date = datetime.utcfromtimestamp(value)

    duration = datetime.utcnow() - date
    minutes = duration.total_seconds() / 60
    hours = duration.total_seconds() / 3600
    print(duration, minutes, hours)
    if minutes < 10:
        return "только что"
    elif minutes < 60:
        return f"{minutes:.0f} минут назад"
    elif hours < 2:
        return f"{hours:.0f} час назад"
    elif hours < 5:
        return f"{hours:.0f} часа назад"
    elif hours < 24:
        return f"{hours:.0f} часов назад"
    elif hours > 24:
        return date.strftime('%Y-%d-%m')


# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    # Ваш код
    return value



