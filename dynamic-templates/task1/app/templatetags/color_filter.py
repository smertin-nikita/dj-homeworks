from django import template

register = template.Library()


@register.filter(name='color')
def color(value, key):
    """Returns cell's color depending of the value"""
    if value == '':
        return 'white'
    else:
        value = float(value)

    if key == 'Суммарная':
        return 'grey'
    elif key != 'Год':
        if value < 0:
            return 'green'
        elif 1 < value < 2:
            return 'red lighten-4'
        elif 2 < value < 5:
            return 'red lighten-3'
        elif value > 5:
            return 'red lighten-1'

    return 'white'

