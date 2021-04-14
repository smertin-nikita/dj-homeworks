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
def format_score(value):
    value = int(value)
    if value < -5:
        return 'все плохо'
    elif -5 <= value < 5:
        return 'неплохо'
    elif 5 <= value:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    value = int(value)
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value <= 50:
        return value
    elif 50 < value:
        return '50+'


@register.filter
def format_selftext(value, count):
    text = value.split(' ')
    return ' '.join(text[:count]) + ' ... ' + ' '.join(text[-count:])



