"""Main module."""

import air

from typing import TYPE_CHECKING, Literal, override

from air.tags.utils import locals_cleanup


class PlotSource(air.UnSafeTag):
    """Provides the plotly dependency"""

    @override
    def __init__(
        self,
        /,
        *,
        version: str = '3.4.0',
        library: str = 'plotly',
        **custom_attributes,
    ):
        self.version = version
        super().__init__('', **custom_attributes | locals_cleanup(locals()))

    @override
    def _render(self) -> str:
        """Wraps the comment text with HTML comment delimiters.

        Returns:
            The serialized comment node.
        """
        return f'<script charset="utf-8" src="https://cdn.plot.ly/plotly-{self.version}.min.js"></script>'
    


class BaseAirPlotTag(air.UnSafeTag):
    """Defines a client-side script.
    Warning: Script tag does not protect against code injection.

    Args:
        text_child: Inline script code. Use an empty string when providing ``src``.
        src: URI of the external script.
        type_: Script type. Examples: ``module``, ``importmap``, ``speculationrules``,
            a JavaScript MIME type (e.g. ``text/javascript``), or empty for classic scripts.
        async_: Fetch in parallel and execute as soon as ready; order is not guaranteed.
        defer: Execute after parsing (classic scripts only; modules defer by default).
        nomodule: Do not execute on browsers that support ES modules.
        crossorigin: CORS mode. One of ``"anonymous"`` or ``"use-credentials"``.
        integrity: Subresource Integrity hash (e.g. ``"sha384-..."``).
        referrerpolicy: Which referrer to send. One of:
            ``"no-referrer"``, ``"no-referrer-when-downgrade"``, ``"origin"``,
            ``"origin-when-cross-origin"``, ``"same-origin"``, ``"strict-origin"``,
            ``"strict-origin-when-cross-origin"``, ``"unsafe-url"``.
        fetchpriority: Network priority hint. One of ``"high"``, ``"low"``, ``"auto"``.
        blocking: Space-separated tokens that block operations; currently ``"render"``.
        attributionsrc: Space-separated URLs for Attribution Reporting (experimental).
        nonce: CSP nonce (meaning: one-time token) to allow this inline script.
        class_: Substituted as the DOM ``class`` attribute.
        id_: DOM ``id`` attribute.
        style: Inline style attribute.
        custom_attributes: Keyword arguments transformed into tag attributes.
    """    

class Line(air.UnSafeTag):
    """Provides the plotly dependency"""

    @override
    def __init__(
        self,
        /,
        *,
        version: str = '3.4.0',
        library: str = 'plotly',
        **custom_attributes,
    ):
        self.version = version
        super().__init__(**custom_attributes | locals_cleanup(locals()))    