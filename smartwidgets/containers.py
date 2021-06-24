from dearpygui import core
from typing import (
    Any,
    Callable,
)

from . import Container

# removed Popup for now


class Window(Container):
    _command: Callable = core.add_window

    def __init__(
        self,
        label: str = None,
        height: int = 200,
        indent: int = -1,
        user_data: Any = None,
        show: bool = True,
        delay_search: str = False,
        min_size: list[int] = [32, 32],
        max_size: list[int] = [30000, 30000],
        menubar: bool = False,
        collapsed: bool = False,
        autosize: bool = False,
        no_resize: bool = False,
        no_title_bar: bool = False,
        no_move: bool = False,
        no_scrollbar: bool = False,
        no_collapse: bool = False,
        horizontal_scrollbar: bool = False,
        no_focus_on_appearing: bool = False,
        no_bring_to_front_on_focus: bool = False,
        no_close: bool = False,
        no_background: bool = False,
        modal: bool = False,
        popup: bool = False,
        on_close: Callable = None,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            user_data=user_data,
            show=show,
            delay_search=delay_search,
            min_size=min_size,
            max_size=max_size,
            menubar=menubar,
            collapsed=collapsed,
            autosize=autosize,
            no_resize=no_resize,
            no_title_bar=no_title_bar,
            no_move=no_move,
            no_scrollbar=no_scrollbar,
            no_collapse=no_collapse,
            horizontal_scrollbar=horizontal_scrollbar,
            no_focus_on_appearing=no_focus_on_appearing,
            no_bring_to_front_on_focus=no_bring_to_front_on_focus,
            no_close=no_close,
            no_background=no_background,
            modal=modal,
            popup=popup,
            on_close=on_close,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.user_data = user_data
        self.show = show
        self.delay_search = delay_search
        self.min_size = min_size
        self.max_size = max_size
        self.menubar = menubar
        self.collapsed = collapsed
        self.autosize = autosize
        self.no_resize = no_resize
        self.no_title_bar = no_title_bar
        self.no_move = no_move
        self.no_scrollbar = no_scrollbar
        self.no_collapse = no_collapse
        self.horizontal_scrollbar = horizontal_scrollbar
        self.no_focus_on_appearing = no_focus_on_appearing
        self.no_bring_to_front_on_focus = no_bring_to_front_on_focus
        self.no_close = no_close
        self.no_background = no_background
        self.modal = modal
        self.popup = popup
        self.on_close = on_close


class Child(Container):
    _command: Callable = core.add_child

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        border: bool = True,
        autosize_x: bool = False,
        autosize_y: bool = False,
        no_scrollbar: bool = False,
        horizontal_scrollbar: bool = False,
        menubar: bool = False,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            border=border,
            autosize_x=autosize_x,
            autosize_y=autosize_y,
            no_scrollbar=no_scrollbar,
            horizontal_scrollbar=horizontal_scrollbar,
            menubar=menubar,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.border = border
        self.autosize_x = autosize_x
        self.autosize_y = autosize_y
        self.no_scrollbar = no_scrollbar
        self.horizontal_scrollbar = horizontal_scrollbar
        self.menubar = menubar


class Theme(Container):
    _command: Callable = core.add_theme

    def __init__(
        self,
        default_theme: bool = False,
        label: str = None,
    ):
        super().__init__(
            default_theme=default_theme,
            label=label,
        )
        self.default_theme = default_theme
        self.label = label


class Clipper(Container):
    _command: Callable = core.add_clipper

    def __init__(
        self,
        show: bool = True,
        parent: int = 0,
        before: int = 0,
        indent: int = -1,
        delay_search: bool = False,
        label: str = None,
    ):
        super().__init__(
            show=show,
            parent=parent,
            before=before,
            indent=indent,
            delay_search=delay_search,
            label=label,
        )
        self.show = show
        self.parent = parent
        self.before = before
        self.indent = indent
        self.delay_search = delay_search
        self.label = label


class FilterSet(Container):
    _command: Callable = core.add_filter_set

    def __init__(
        self,
        show: bool = True,
        parent: int = 0,
        before: int = 0,
        indent: int = -1,
        delay_search: bool = False,
        label: str = None,
    ):
        super().__init__(
            show=show,
            parent=parent,
            before=before,
            indent=indent,
            delay_search=delay_search,
            label=label,
        )
        self.show = show
        self.parent = parent
        self.before = before
        self.indent = indent
        self.delay_search = delay_search
        self.label = label


class DragPayload(Container):
    _command: Callable = core.add_drag_payload

    def __init__(
        self,
        show: bool = True,
        parent: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_data: Any = None,
        label: str = None,
    ):
        super().__init__(
            show=show,
            parent=parent,
            payload_type=payload_type,
            drag_data=drag_data,
            label=label,
        )
        self.show = show
        self.parent = parent
        self.payload_type = payload_type
        self.drag_data = drag_data
        self.label = label


class FileDialog(Container):
    _command: Callable = core.add_file_dialog

    def __init__(
        self,
        height: int = 0,
        label: str = '',
        callback: Callable = None,
        show: bool = True,
        default_path: str = '',
        default_filename: str = '.',
        file_count: int = 0,
        modal: bool = False,
        directory_selector: bool = False,
    ):
        super().__init__(
            height=height,
            label=label,
            callback=callback,
            show=show,
            default_path=default_path,
            default_filename=default_filename,
            file_count=file_count,
            modal=modal,
            directory_selector=directory_selector,
        )
        self.height = height
        self.label = label
        self.callback = callback
        self.show = show
        self.default_path = default_path
        self.default_filename = default_filename
        self.file_count = file_count
        self.modal = modal
        self.directory_selector = directory_selector


class Table(Container):
    _command: Callable = core.add_table

    def __init__(
        self,
        header_row: bool = True,
        height: int = 0,
        show: bool = True,
        parent: int = 0,
        before: int = 0,
        resizable: bool = False,
        reorderable: bool = False,
        sortable: bool = False,
        context_menu_in_body: bool = False,
        row_background: bool = False,
        borders_innerH: bool = False,
        borders_outerH: bool = False,
        borders_innerV: bool = False,
        borders_outerV: bool = False,
        policy: int = 0,
        no_host_extendX: bool = False,
        no_host_extendY: bool = False,
        no_keep_columns_visible: bool = False,
        no_clip: bool = False,
        pad_outerX: bool = False,
        no_pad_outerX: bool = False,
        no_pad_innerX: bool = False,
        scrollX: bool = False,
        scrollY: bool = False,
        indent: str = -1,
        callback: Callable = None,
        sort_multi: bool = False,
        sort_tristate: bool = False,
        pos: str = [],
        freeze_rows: int = 0,
        freeze_columns: int = 0,
        delay_search: bool = False,
        label: str = None,
    ):
        super().__init__(
            header_row=header_row,
            height=height,
            show=show,
            parent=parent,
            before=before,
            resizable=resizable,
            reorderable=reorderable,
            sortable=sortable,
            context_menu_in_body=context_menu_in_body,
            row_background=row_background,
            borders_innerH=borders_innerH,
            borders_outerH=borders_outerH,
            borders_innerV=borders_innerV,
            borders_outerV=borders_outerV,
            policy=policy,
            no_host_extendX=no_host_extendX,
            no_host_extendY=no_host_extendY,
            no_keep_columns_visible=no_keep_columns_visible,
            no_clip=no_clip,
            pad_outerX=pad_outerX,
            no_pad_outerX=no_pad_outerX,
            no_pad_innerX=no_pad_innerX,
            scrollX=scrollX,
            scrollY=scrollY,
            indent=indent,
            callback=callback,
            sort_multi=sort_multi,
            sort_tristate=sort_tristate,
            pos=pos,
            freeze_rows=freeze_rows,
            freeze_columns=freeze_columns,
            delay_search=delay_search,
            label=label,
        )
        self.header_row = header_row
        self.height = height
        self.show = show
        self.parent = parent
        self.before = before
        self.resizable = resizable
        self.reorderable = reorderable
        self.sortable = sortable
        self.context_menu_in_body = context_menu_in_body
        self.row_background = row_background
        self.borders_innerH = borders_innerH
        self.borders_outerH = borders_outerH
        self.borders_innerV = borders_innerV
        self.borders_outerV = borders_outerV
        self.policy = policy
        self.no_host_extendX = no_host_extendX
        self.no_host_extendY = no_host_extendY
        self.no_keep_columns_visible = no_keep_columns_visible
        self.no_clip = no_clip
        self.pad_outerX = pad_outerX
        self.no_pad_outerX = no_pad_outerX
        self.no_pad_innerX = no_pad_innerX
        self.scrollX = scrollX
        self.scrollY = scrollY
        self.indent = indent
        self.callback = callback
        self.sort_multi = sort_multi
        self.sort_tristate = sort_tristate
        self.pos = pos
        self.freeze_rows = freeze_rows
        self.freeze_columns = freeze_columns
        self.delay_search = delay_search
        self.label = label


class Drawlist(Container):
    _command: Callable = core.add_drawlist

    def __init__(
        self,
        height: int = 0,
        show: bool = True,
        parent: int = 0,
        before: int = 0,
        callback: Callable = None,
        user_data: Any = None,
        pos: str = [],
        delay_search: bool = False,
        label: str = None,
    ):
        super().__init__(
            height=height,
            show=show,
            parent=parent,
            before=before,
            callback=callback,
            user_data=user_data,
            pos=pos,
            delay_search=delay_search,
            label=label,
        )
        self.height = height
        self.show = show
        self.parent = parent
        self.before = before
        self.callback = callback
        self.user_data = user_data
        self.pos = pos
        self.delay_search = delay_search
        self.label = label


class ViewportDrawlist(Container):
    _command: Callable = core.add_viewport_drawlist

    def __init__(
        self,
        front: bool = True,
        show: bool = True,
        delay_search: bool = False,
        label: str = None,
    ):
        super().__init__(
            front=front,
            show=show,
            delay_search=delay_search,
            label=label,
        )
        self.front = front
        self.show = show
        self.delay_search = delay_search
        self.label = label


class TableRow(Container):
    _command: Callable = core.add_table_row

    def __init__(
        self,
        show: bool = True,
        parent: int = 0,
        before: int = 0,
        height: int = 0,
        label: str = None,
    ):
        super().__init__(
            show=show,
            parent=parent,
            before=before,
            height=height,
            label=label,
        )
        self.show = show
        self.parent = parent
        self.before = before
        self.height = height
        self.label = label


class DrawLayer(Container):
    _command: Callable = core.add_draw_layer

    def __init__(
        self,
        show: bool = True,
        parent: int = 0,
        before: int = 0,
        label: str = None,
    ):
        super().__init__(
            show=show,
            parent=parent,
            before=before,
            label=label,
        )
        self.show = show
        self.parent = parent
        self.before = before
        self.label = label


class MenuBar(Container):
    _command: Callable = core.add_menu_bar

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        show: bool = True,
        delay_search: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            show=show,
            delay_search=delay_search,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.show = show
        self.delay_search = delay_search


class Menu(Container):
    _command: Callable = core.add_menu

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        enabled: bool = True,
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            enabled=enabled,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.enabled = enabled
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset


class CollapsingHeader(Container):
    _command: Callable = core.add_collapsing_header

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        closable: bool = False,
        default_open: bool = False,
        open_on_double_click: bool = False,
        open_on_arrow: bool = False,
        leaf: bool = False,
        bullet: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            closable=closable,
            default_open=default_open,
            open_on_double_click=open_on_double_click,
            open_on_arrow=open_on_arrow,
            leaf=leaf,
            bullet=bullet,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.closable = closable
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet


class Group(Container):
    _command: Callable = core.add_group

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        horizontal: bool = False,
        horizontal_spacing: float = -1.0,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            horizontal=horizontal,
            horizontal_spacing=horizontal_spacing,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.horizontal = horizontal
        self.horizontal_spacing = horizontal_spacing


class Node(Container):
    _command: Callable = core.add_node

    def __init__(
        self,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        draggable: bool = True,
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            draggable=draggable,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.draggable = draggable


class NodeAttribute(Container):
    _command: Callable = core.add_node_attribute

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        output: bool = False,
        static: bool = False,
        shape: int = 0,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            output=output,
            static=static,
            shape=shape,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.output = output
        self.static = static
        self.shape = shape


class NodeEditor(Container):
    _command: Callable = core.add_node_editor

    def __init__(
        self,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        delink_callback: Callable = None,
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            delink_callback=delink_callback,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.delink_callback = delink_callback


class StagingContainer(Container):
    _command: Callable = core.add_staging_container

    def __init__(
        self,
        label: str = None,
    ):
        super().__init__(
            label=label,
        )
        self.label = label


class TabBar(Container):
    _command: Callable = core.add_tab_bar

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        reorderable: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            reorderable=reorderable,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.reorderable = reorderable


class Tab(Container):
    _command: Callable = core.add_tab

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        closable: bool = False,
        no_reorder: bool = False,
        leading: bool = False,
        trailing: bool = False,
        no_tooltip: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            closable=closable,
            no_reorder=no_reorder,
            leading=leading,
            trailing=trailing,
            no_tooltip=no_tooltip,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.closable = closable
        self.no_reorder = no_reorder
        self.leading = leading
        self.trailing = trailing
        self.no_tooltip = no_tooltip


class TreeNode(Container):
    _command: Callable = core.add_tree_node

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        default_open: bool = False,
        open_on_double_click: bool = False,
        open_on_arrow: bool = False,
        leaf: bool = False,
        bullet: bool = False,
        selectable: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            default_open=default_open,
            open_on_double_click=open_on_double_click,
            open_on_arrow=open_on_arrow,
            leaf=leaf,
            bullet=bullet,
            selectable=selectable,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_open = default_open
        self.open_on_double_click = open_on_double_click
        self.open_on_arrow = open_on_arrow
        self.leaf = leaf
        self.bullet = bullet
        self.selectable = selectable


class Tooltip(Container):
    _command: Callable = core.add_tooltip

    def __init__(
        self,
        label: str = None,
        show: bool = True,
    ):
        super().__init__(
            label=label,
            show=show,
        )
        self.label = label
        self.show = show


class Plot(Container):
    _command: Callable = core.add_plot

    def __init__(
        self,
        label: str = None,
        height: int = 400,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        no_title: bool = False,
        no_menus: bool = False,
        no_box_select: bool = False,
        no_mouse_pos: bool = False,
        no_highlight: bool = False,
        no_child: bool = False,
        query: bool = False,
        crosshairs: bool = False,
        anti_aliased: bool = False,
        equal_aspects: bool = False,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            no_title=no_title,
            no_menus=no_menus,
            no_box_select=no_box_select,
            no_mouse_pos=no_mouse_pos,
            no_highlight=no_highlight,
            no_child=no_child,
            query=query,
            crosshairs=crosshairs,
            anti_aliased=anti_aliased,
            equal_aspects=equal_aspects,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.delay_search = delay_search
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_title = no_title
        self.no_menus = no_menus
        self.no_box_select = no_box_select
        self.no_mouse_pos = no_mouse_pos
        self.no_highlight = no_highlight
        self.no_child = no_child
        self.query = query
        self.crosshairs = crosshairs
        self.anti_aliased = anti_aliased
        self.equal_aspects = equal_aspects
