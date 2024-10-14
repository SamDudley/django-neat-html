# django-neat-html

Integrate `neat-html` as a template backend for Django.

## Examples

- [counter](example/neats/pages/counter.py)

## Installation

Using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install django-neat-html
```

## Configuration

Add the `django_neat_html.NeatHtml` template backend.

```python
# my_project/settings.py

TEMPLATES = [
    ...
    {
        'NAME': 'neat_html',
        'BACKEND': 'django_neat_html.NeatHtml',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]
```

## Usage

Write some components using the `neat-html` package.

```python
# my_project/my_app/neats/components.py

from neat_html import Element, h

def my_page(context) -> Element:
    return h("h1", "My page")
```

Reference them as a template in your Django views.

```python
# my_project/my_app/views.py

from django.template.response import TemplateResponse

def my_view(request):
    return TemplateResponse(request, "my_project.my_app.neats.component.my_page", {})
```
