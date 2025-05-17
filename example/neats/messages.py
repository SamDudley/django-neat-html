from neat_html import Element, h
from django_neat_html import context


def messages() -> Element:
    return h("ul", [h("li", str(msg)) for msg in context.messages])
