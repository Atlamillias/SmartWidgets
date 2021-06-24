from abc import ABCMeta, abstractmethod
from typing import Callable

from dearpygui import core


# needs handler & theme support
class Widget(metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    __config = set()

    def __init__(self, **kwargs):
        # parent was previously handled
        # via property, but this approach
        # is much better
        if parent := kwargs.pop("parent", None):
            if isinstance(parent, Container):
                core.push_container_stack(parent)
            else:
                kwargs["parent"] = parent.id
                parent = None

        self.__id = self._command(**kwargs)

        if parent:
            core.pop_container_stack()

        [self.__config.add(optn) for optn in kwargs.keys()]

    def __str__(self):
        return f"{self.__id}"

    def __repr__(self):
        mVAppType = core.get_item_info(self.id)["type"].lstrip('::')[-1]
        return f"{self.__class__.__qualname__} ({type(self)}) => \
            (<{mVAppType} '{self.__id}'>)"

    def __getattr__(self, attr):
        if attr in self.__config:
            try:
                return core.get_item_configuration(self.__id)[attr]
            except KeyError:
                return super().__getattr__(attr)

        return super().__getattr__(attr)

    def __setattr__(self, attr, value):
        # Not setting config attrs after creation
        # might interfere with editing attrs like
        # lists, dicts, etc because they would only
        # be changed, not set.
        # i.e. __iadd__, .append for a list value
        if attr in self.__config:
            core.configure_item(self.__id, **{attr: value})
        else:
            # might have to un-nest (above comment)
            super().__setattr__(attr, value)

    @property
    def id(self):
        return self.__id

    @property
    def state(self):
        """Return the current state of the widget."""
        return core.get_item_state(self.__id)

    @property
    def value(self):
        """Return the widget value (if any)."""
        return core.get_value(self.__id)

    def move_up(self):
        core.move_item_up(self.__id)

    def move_down(self):
        core.move_item_down(self.__id)

    def move(self, parent: int, before: int):
        """Move a widget to another <parent> before <before>."""
        core.move_item(self.__id, parent, before)

    def refresh(self):
        """Deletes all children in the widget, if any."""
        core.delete_item(self.__id, children_only=True)

    def remove(self):
        """Deletes the widget (and children)."""
        core.delete_item(self.__id)

    def configure(self, **config):
        """Updates the widget configuration."""
        core.configure_item(self.__id, **config)

    def configuration(self, option=None):
        """Returns the entire current widget configuration, or
        only <option> (if specified)."""
        if option:
            return core.get_item_configuration(self.__id)[option]

        return core.get_item_configuration(self.__id)


class Container(Widget, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable: ...

    def __enter__(self):
        core.push_container_stack(self.id)
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        core.pop_container_stack(self.id)
