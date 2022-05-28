from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def author_details(author):
  if not isinstance(author, User):
    # Return empty string as safe default
    return ""
  
  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"

  if author.email:
    email = author.email
    prefix = f'<a href="mailto:{email}">'
    suffix = "</a>"
  else:
    prefix = ""
    suffix = ""
  
  return f"{prefix}{name}{suffix}"