from django import template

register = template.Library()

@register.filter
def duration_format(value):
    try:
        value = int(value)
        minutes = value // 60
        seconds = value % 60
        return f"{minutes}min {seconds:02}sec"
    except (ValueError, TypeError):
        return value