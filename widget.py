from abc import ABCMeta, abstractmethod
from typing import Callable

from dearpygui import dearpygui as dpg
from item import Item, ContextSupport


class Widget(Item, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Container(Widget, ContextSupport, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...
