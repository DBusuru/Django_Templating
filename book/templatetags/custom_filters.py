from django import template

register = template.Library()

@register.filter
def split(value, key=","):
    """Splits the string by the given key (default is comma)."""
    # Be defensive: if value is None or empty, return an empty list
    try:
        if value is None:
            return []
        # If it's not a string, coerce to string so split works
        if not isinstance(value, str):
            value = str(value)
        return value.split(key)
    except Exception:
        return []


@register.filter
def trim(value):
    """Trim whitespace from both ends of a string. If value is None, return empty string."""
    if value is None:
        return ""
    try:
        return str(value).strip()
    except Exception:
        return value
