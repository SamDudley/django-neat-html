from .base import page

from neats.forms import form


def main(context):
    return page(
        title="home - django-neat-html",
        content=[
            form(
                "first_name",
                "last_name",
                "email",
                "password",
            ),
        ],
    )
