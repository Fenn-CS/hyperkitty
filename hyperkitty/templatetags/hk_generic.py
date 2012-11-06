import datetime
import re

from django import template
from django.utils.datastructures import SortedDict

register = template.Library()


@register.filter
def trimString(str):
    return re.sub('\s+', ' ', str)


@register.filter(name='sort')
def listsort(value):
    if isinstance(value, dict):
        new_dict = SortedDict()
        key_list = value.keys()
        key_list.sort()
        key_list.reverse()
        for key in key_list:
            values = value[key]
            values.sort()
            values.reverse()
            new_dict[key] = values
        return new_dict.items()
    elif isinstance(value, list):
        new_list = list(value)
        new_list.sort()
        return new_list
    else:
        return value
    listsort.is_safe = True


@register.filter(name="monthtodate")
def to_date(month, year):
    return datetime.date(year, month, 1)


@register.filter
def strip_page(value):
    print repr(value), repr(value)[-2]
    if not value:
        return value
    if value.endswith('/') and value[-3] == '/':
        end_with_number = False
        try:
            if int(value[-2]) in range(0,10):
                end_with_number = True
            if end_with_number:
                output = value.rsplit('/', 2)
        except ValueError:
            output = value.rsplit('/', 1)
    else:
        output = value.rsplit('/', 1)
    return output[0]


# From http://djangosnippets.org/snippets/1259/
@register.filter
def truncatesmart(value, limit=80):
    """
    Truncates a string after a given number of chars keeping whole words.

    Usage:
        {{ string|truncatesmart }}
        {{ string|truncatesmart:50 }}
    """
    try:
        limit = int(limit)
    # invalid literal for int()
    except ValueError:
        # Fail silently.
        return value

    # Make sure it's unicode
    value = unicode(value)

    # Return the string itself if length is smaller or equal to the limit
    if len(value) <= limit:
        return value

    # Cut the string
    value = value[:limit]

    # Break into words and remove the last
    words = value.split(' ')[:-1]

    # Join the words and return
    return ' '.join(words) + '...'


MAILTO_RE = re.compile("<a href=['\"]mailto:([^'\"]+)@([^'\"]+)['\"]>[^<]+</a>")
@register.filter(is_safe=True)
def escapeemail(text):
    """To escape email addresses"""
    # reverse the effect of urlize() on email addresses
    text = MAILTO_RE.sub(r"\1(a)\2", text)
    return text.replace("@", u"\uff20")
