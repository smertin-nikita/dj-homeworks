from django import template


register = template.Library()


@register.inclusion_tag('app/menu.html')
def show_menu(active_page=None):
    if active_page:
        context = dict()
        context[active_page] = 'class=active'
        return context




