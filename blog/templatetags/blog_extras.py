from django import template
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter
def author_details(author):
  if not isinstance(author, User):
    # Return empty string as safe default
    return ""
  
  if author.first_name and author.last_name:
    name = escape(f"{author.first_name} {author.last_name}")
  else:
    name = escape(f"{author.username}")

  if author.email:
    email = escape(author.email)
    prefix = f'<a href="mailto:{email}">'
    suffix = "</a>"
  else:
    prefix = ""
    suffix = ""
  
  return mark_safe(f"{prefix}{name}{suffix}")