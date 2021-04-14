from django import template


register = template.Library()


@register.inclusion_tag('app/menu.html')
def show_menu(active_page=None):
    """
    :param active_page: Активная страница. Название шаблона который отображается
    :return:
    """
    if active_page:
        context = dict()
        context[active_page] = 'class=active'
        return context




