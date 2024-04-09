from neat_html import h, Element


# TODO: Move to neat_html.
def base_page(
    head: Element | list[Element],
    body: Element | list[Element],
    lang: str = "en",
) -> Element:
    return [
        h("!DOCTYPE", {"html": True}),
        h(
            "html",
            {"lang": lang},
            [
                h("head", head),
                h("body", body),
            ],
        ),
    ]
