from django_neat_html.utils import base_page
from neat_html import Element, h


def page(title: str, content: Element | list[Element]) -> Element:
    return base_page(
        head=[
            h("meta", {"charset": "UTF-8"}),
            h(
                "meta",
                {
                    "name": "viewport",
                    "content": "width=device-width, initial-scale=1.0",
                },
            ),
            h("title", title),
        ],
        body=[
            h("main", content),
        ],
    )
