# django-neat-html

Integrate neat-html as a template backend for Django.

## Example

```python
# my_app/neats/page/counter.py

from neat_html import h, safe

from my_app.service.counter import get_count, inc_count

from .base import page


def counter():
    return h("p", get_count())


def increment(context):
    return h(
        "form",
        {"method": "post"},
        [
            safe(context["csrf_input"]),
            h("button", {"type": "submit"} "+"),
        ]
    )


def main(context):
    return page(
        title="Counter example",
        content=[
            counter(),
            increment(context),
        ]
    )


# my_app/views.py

def counter(request):
    if request.method == "POST":
        inc_count()

    return TemplateResponse(request, "my_app.neats.page.counter.main", {})


# my_app/urls.py

url_patterns = [
    path("counter", views.counter, name="counter"),
]
```
