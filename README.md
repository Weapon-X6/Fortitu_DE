![example branch parameter](https://github.com/Weapon-X6/Fortitu_DE/actions/workflows/django.yml/badge.svg)
[![codecov](https://codecov.io/gh/Weapon-X6/Fortitu_DE/graph/badge.svg?token=1F8BF5T9NE)](https://codecov.io/gh/Weapon-X6/Fortitu_DE)

# Blango Blog

### Features

* Allows reading blog posts
* Allows adding/updating/deleting posts and adding comments on posts for authenticated users
* Allows login using Google credentials through the OAuth 2.0 protocol
* Use [Markdown](https://www.markdownguide.org/basic-syntax/) instead of html tags to format the blog posts when adding

### Installation

Install dependencies
```
python -m pip install -r requirements.txt
```

If using Windows
```
pip uninstall python-magic -y    
```

Run migrations

```
python manage.py migrate
```

### Execution

To play around change in *manage.py* the environment from "Prod" to "Dev".

Finally:
```
python manage.py runserver
```
