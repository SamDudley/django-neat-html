from neat_html import h, Element


def form(*fields: str) -> Element:
    inputs = [
        h(
            "div",
            field(
                name,
                f"id_{name}",
                name.replace("_", " ").capitalize(),
                "text",
            ),
        )
        for name in fields
    ]

    return h("form", [*inputs, h("button", "Submit")])


def field(name: str, id: str, label: str, type: str) -> list[Element]:
    return [
        h("label", {"for": id}, label),
        h("input", {"name": name, "type": type, id: "id"}),
    ]
