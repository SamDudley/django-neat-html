from collections.abc import Callable
from typing import Any

from asgiref.local import Local
from django.http import HttpRequest
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from django.utils.functional import cached_property
from django.utils.module_loading import import_string

from neat_html import Element, render


_context = Local()
context = _context


class NeatHtml(BaseEngine):
    def __init__(self, params: dict[str, Any]):
        params = params.copy()
        self.options = params.pop("OPTIONS")
        super().__init__(params)

        self.context_processors = self.options.pop("context_processors", [])

    def get_template(self, template_name: str) -> "Template":
        return Template(import_string(template_name), self)

    @cached_property
    def template_context_processors(self):
        return [import_string(path) for path in self.context_processors]


class Template:
    def __init__(self, template: Callable[..., Element], backend: NeatHtml) -> None:
        self.template = template
        self.backend = backend

    def render(
        self, context: dict[str, Any] | None = None, request: HttpRequest | None = None
    ) -> str:
        if context is None:
            context = {}
        if request is not None:
            context["request"] = request
            context["csrf_input"] = csrf_input_lazy(request)
            context["csrf_token"] = csrf_token_lazy(request)
            for context_processor in self.backend.template_context_processors:
                context.update(context_processor(request))

        for key, value in context.items():
            setattr(_context, key, value)

        return render(self.template(context))
