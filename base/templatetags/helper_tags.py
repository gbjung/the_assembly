from django import template

register = template.Library()

@register.simple_tag
def unwrap_authors(authors):
    authors = ','.join([str(author) for author in authors])
    return authors
