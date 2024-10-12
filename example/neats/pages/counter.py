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
