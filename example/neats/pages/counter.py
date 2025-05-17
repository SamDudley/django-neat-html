from django.contrib import messages
from django.template.response import TemplateResponse
from django_neat_html import context
from neat_html import h, safe, Element

from neats.messages import messages as messages_component
from .base import page


# Service


COUNTER: int = 0


def get_count() -> int:
    return COUNTER


def inc_count() -> int:
    global COUNTER
    COUNTER += 1
    return COUNTER


# Components


def counter() -> Element:
    return h("p", str(get_count()))


def increment() -> Element:
    return h(
        "form",
        {"method": "post"},
        [
            safe(context.csrf_input),
            h("button", {"type": "submit"}, "+"),
        ],
    )


def main(context) -> Element:
    return page(
        title="Counter example",
        content=[
            messages_component(),
            counter(),
            increment(),
        ],
    )


# Views


def counter_view(request):
    if request.method == "POST":
        count = inc_count()
        messages.add_message(request, messages.INFO, f"Count incremented to {count}.")
    return TemplateResponse(request, "neats.pages.counter.main", {})
