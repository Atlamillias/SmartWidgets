from typing import (
    Callable,
)

from dearpygui import core

from .bases import Container


class FontRegistry(Container):
    _command: Callable = core.add_font_registry

    def __init__(
        self,
        show: bool = True,
        label: str = None,
    ):
        super().__init__(
            show=show,
            label=label,
        )
        self.show = show
        self.label = label


class HandlerRegistry(Container):
    _command: Callable = core.add_handler_registry

    def __init__(
        self,
        show: bool = True,
        label: str = None,
    ):
        super().__init__(
            show=show,
            label=label,
        )
        self.show = show
        self.label = label


class TextureRegistry(Container):
    _command: Callable = core.add_texture_registry

    def __init__(
        self,
        show: bool = True,
        label: str = None,
    ):
        super().__init__(
            show=show,
            label=label,
        )
        self.show = show
        self.label = label
