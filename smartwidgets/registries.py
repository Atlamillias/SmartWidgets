from typing import Callable
from abc import abstractmethod, ABCMeta

from dearpygui import core as dpg

from .bases import Container


class RegistryPropertiesMixin:
    __fonts = None
    __handlers = None
    __textures = None
    __values = None




class Registry(Container, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(
        self,
        show: bool = True,
        label: str = None,
        **kwargs,
    ):
        super().__init__(
            show=show,
            label=label,
            **kwargs
        )
        self.show = show
        self.label = label


class FontRegistry(Registry):
    _command = dpg.add_font_registry

class HandlerRegistry(Registry):
    _command = dpg.add_handler_registry

class TextureRegistry(Registry):
    _command = dpg.add_texture_registry

class ValueRegistry(Container):  # excludes "show"/"enabled"
    _command = dpg.add_value_registry

    def __init__(self, label: str = None, **kwargs):
        super().__init__(label=label, **kwargs)
        self.label = label
