from collections.abc import Callable
from typing import Any

from django.http import HttpRequest
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from django.utils.module_loading import import_string

from neat_html import Element, render


class Template:
    def __init__(self, template: Callable[..., Element]) -> None:
        self.template = template

    def render(
        self, context: dict[str, Any] | None = None, request: HttpRequest | None = None
    ) -> str:
        if context is None:
            context = {}
        if request is not None:
            context["request"] = request
            context["csrf_input"] = csrf_input_lazy(request)
            context["csrf_token"] = csrf_token_lazy(request)
        return render(self.template(context))


class NeatHtml(BaseEngine):
    def __init__(self, params: dict[str, Any]):
        params = params.copy()
        params.pop("OPTIONS")
        super().__init__(params)

    def get_template(self, template_name: str) -> Template:
        return Template(import_string(template_name))
