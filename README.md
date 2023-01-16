# blango Blog

### Features

* Allows reading blog posts
* Allows sign up
* Allows adding/updating/deleting posts and adding comments on posts for authenticated users
* Implement third-party integration to login using Google
* Use [Markdown](https://www.markdownguide.org/basic-syntax/) instead of html tags to format the blog posts when adding

### Installation

Install dependencies
```
python -m pip install -r requirements.txt
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
