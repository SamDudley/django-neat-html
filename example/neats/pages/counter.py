from django.template.response import TemplateResponse
from django_neat_html import context
from neat_html import h, safe

from .base import page


# Service


COUNTER: int = 0


def get_count() -> int:
    return COUNTER


def inc_count() -> None:
    global COUNTER
    COUNTER += 1


# Components


def counter():
    return h("p", str(get_count()))


def increment():
    return h(
        "form",
        {"method": "post"},
        [
            safe(context.csrf_input),
            h("button", {"type": "submit"}, "+"),
        ],
    )


def main(context):
    return page(
        title="Counter example",
        content=[
            counter(),
            increment(),
        ],
    )


# Views


def counter_view(request):
    if request.method == "POST":
        inc_count()
    return TemplateResponse(request, "neats.pages.counter.main", {})
