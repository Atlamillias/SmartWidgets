from typing import (
    Callable,
    Any,
)

from dearpygui import core

from .bases import Widget


class HistogramSeries(Widget):
    _command: Callable = core.add_2d_histogram_series

    def __init__(
        self,
        x: list[float],
        y: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        xbins: int = -1,
        ybins: int = -1,
        xmin_range: float = 0.0,
        xmax_range: float = 1.0,
        ymin_range: float = 0.0,
        ymax_range: float = 1.0,
        density: bool = False,
        outliers: bool = True,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            xbins=xbins,
            ybins=ybins,
            xmin_range=xmin_range,
            xmax_range=xmax_range,
            ymin_range=ymin_range,
            ymax_range=ymax_range,
            density=density,
            outliers=outliers,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.xbins = xbins
        self.ybins = ybins
        self.xmin_range = xmin_range
        self.xmax_range = xmax_range
        self.ymin_range = ymin_range
        self.ymax_range = ymax_range
        self.density = density
        self.outliers = outliers
        self.contribute_to_bounds = contribute_to_bounds


class ThiccSlider(Widget):
    _command: Callable = core.add_3d_slider

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[float] = [0.0,0.0,0.0,0.0],
        max_x: float = 100.0,
        max_y: float = 100.0,
        max_z: float = 100.0,
        min_x: float = 0.0,
        min_y: float = 0.0,
        min_z: float = 0.0,
        scale: float = 1.0,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            max_x=max_x,
            max_y=max_y,
            max_z=max_z,
            min_x=min_x,
            min_y=min_y,
            min_z=min_z,
            scale=scale,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z
        self.min_x = min_x
        self.min_y = min_y
        self.min_z = min_z
        self.scale = scale


class AreaSeries(Widget):
    _command: Callable = core.add_area_series

    def __init__(
        self,
        x: list[float],
        y: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        fill: list[int] = [0,0,0,-255],
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            fill=fill,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.fill = fill
        self.contribute_to_bounds = contribute_to_bounds


class BarSeries(Widget):
    _command: Callable = core.add_bar_series

    def __init__(
        self,
        x: list[float],
        y: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        weight: float = 1.0,
        horizontal: bool = False,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            weight=weight,
            horizontal=horizontal,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.weight = weight
        self.horizontal = horizontal
        self.contribute_to_bounds = contribute_to_bounds


class Button(Widget):
    _command: Callable = core.add_button

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        small: bool = False,
        arrow: bool = False,
        direction: int = 0,
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
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            small=small,
            arrow=arrow,
            direction=direction,
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
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.small = small
        self.arrow = arrow
        self.direction = direction


class CandleSeries(Widget):
    _command: Callable = core.add_candle_series

    def __init__(
        self,
        dates: list[float],
        opens: list[float],
        closes: list[float],
        lows: list[float],
        highs: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        bull_color: list[int] = [0,255,113,255],
        bear_color: list[int] = [218,13,79,255],
        weight: int = 0.25,
        contribute_to_bounds: bool = True,
        tooltip: bool = True,
    ):
        super().__init__(
            dates=dates,
            opens=opens,
            closes=closes,
            lows=lows,
            highs=highs,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            bull_color=bull_color,
            bear_color=bear_color,
            weight=weight,
            contribute_to_bounds=contribute_to_bounds,
            tooltip=tooltip,
        )
        self.dates = dates
        self.opens = opens
        self.closes = closes
        self.lows = lows
        self.highs = highs
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.bull_color = bull_color
        self.weight = weight
        self.contribute_to_bounds = contribute_to_bounds
        self.tooltip = tooltip


class Checkbox(Widget):
    _command: Callable = core.add_checkbox

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value


class ColorButton(Widget):
    _command: Callable = core.add_color_button

    def __init__(
        self,
        default_value: list[int] = [0,0,0,255],
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        no_alpha: bool = False,
        no_border: bool = False,
        no_drag_drop: bool = False,
    ):
        super().__init__(
            default_value=default_value,
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
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            no_alpha=no_alpha,
            no_border=no_border,
            no_drag_drop=no_drag_drop,
        )
        self.default_value = default_value
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
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_alpha = no_alpha
        self.no_border = no_border
        self.no_drag_drop = no_drag_drop


class ColorEdit(Widget):
    _command: Callable = core.add_color_edit

    def __init__(
        self,
        default_value: list[int] = [0,0,0,255],
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        no_alpha: bool = False,
        no_picker: bool = False,
        no_options: bool = False,
        no_small_preview: bool = False,
        no_inputs: bool = False,
        no_tooltip: bool = False,
        no_label: bool = False,
        no_drag_drop: bool = False,
        alpha_bar: bool = False,
        alpha_preview: bool = False,
        alpha_preview_half: bool = False,
        display_rgb: bool = False,
        display_hsv: bool = False,
        display_hex: bool = False,
        uint8: bool = False,
        floats: bool = False,
        input_rgb: bool = False,
        input_hsv: bool = False,
        m_3component: bool = False,
    ):
        super().__init__(
            default_value=default_value,
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            no_alpha=no_alpha,
            no_picker=no_picker,
            no_options=no_options,
            no_small_preview=no_small_preview,
            no_inputs=no_inputs,
            no_tooltip=no_tooltip,
            no_label=no_label,
            no_drag_drop=no_drag_drop,
            alpha_bar=alpha_bar,
            alpha_preview=alpha_preview,
            alpha_preview_half=alpha_preview_half,
            display_rgb=display_rgb,
            display_hsv=display_hsv,
            display_hex=display_hex,
            uint8=uint8,
            floats=floats,
            input_rgb=input_rgb,
            input_hsv=input_hsv,
            m_3component=m_3component,
        )
        self.default_value = default_value
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_alpha = no_alpha
        self.no_picker = no_picker
        self.no_options = no_options
        self.no_small_preview = no_small_preview
        self.no_inputs = no_inputs
        self.no_tooltip = no_tooltip
        self.no_label = no_label
        self.no_drag_drop = no_drag_drop
        self.alpha_bar = alpha_bar
        self.alpha_preview = alpha_preview
        self.alpha_preview_half = alpha_preview_half
        self.display_rgb = display_rgb
        self.display_hsv = display_hsv
        self.display_hex = display_hex
        self.uint8 = uint8
        self.floats = floats
        self.input_rgb = input_rgb
        self.input_hsv = input_hsv
        self.m_3component = m_3component


class ColorPicker(Widget):
    _command: Callable = core.add_color_picker

    def __init__(
        self,
        default_value: list[int] = [0,0,0,255],
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        no_alpha: bool = False,
        no_picker: bool = False,
        no_small_preview: bool = False,
        no_inputs: bool = False,
        no_tooltip: bool = False,
        no_label: bool = False,
        alpha_bar: bool = False,
        alpha_preview: bool = False,
        alpha_preview_half: bool = False,
        display_rgb: bool = False,
        display_hsv: bool = False,
        display_hex: bool = False,
        uint8: bool = False,
        floats: bool = False,
        input_rgb: bool = False,
        input_hsv: bool = False,
        picker_hue_bar: bool = False,
        picker_hue_wheel: bool = False,
    ):
        super().__init__(
            default_value=default_value,
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            no_alpha=no_alpha,
            no_picker=no_picker,
            no_small_preview=no_small_preview,
            no_inputs=no_inputs,
            no_tooltip=no_tooltip,
            no_label=no_label,
            alpha_bar=alpha_bar,
            alpha_preview=alpha_preview,
            alpha_preview_half=alpha_preview_half,
            display_rgb=display_rgb,
            display_hsv=display_hsv,
            display_hex=display_hex,
            uint8=uint8,
            floats=floats,
            input_rgb=input_rgb,
            input_hsv=input_hsv,
            picker_hue_bar=picker_hue_bar,
            picker_hue_wheel=picker_hue_wheel,
        )
        self.default_value = default_value
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.no_alpha = no_alpha
        self.no_picker = no_picker
        self.no_small_preview = no_small_preview
        self.no_inputs = no_inputs
        self.no_tooltip = no_tooltip
        self.no_label = no_label
        self.alpha_bar = alpha_bar
        self.alpha_preview = alpha_preview
        self.alpha_preview_half = alpha_preview_half
        self.display_rgb = display_rgb
        self.display_hsv = display_hsv
        self.display_hex = display_hex
        self.uint8 = uint8
        self.floats = floats
        self.input_rgb = input_rgb
        self.input_hsv = input_hsv
        self.picker_hue_bar = picker_hue_bar
        self.picker_hue_wheel = picker_hue_wheel


class ColormapScale(Widget):
    _command: Callable = core.add_colormap_scale

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        pos: list[int] = [],
        default_value: int = 0,
        min_scale: float = 0.0,
        max_scale: float = 1.0,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            show=show,
            pos=pos,
            default_value=default_value,
            min_scale=min_scale,
            max_scale=max_scale,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.pos = pos
        self.default_value = default_value
        self.min_scale = min_scale
        self.max_scale = max_scale


class Combo(Widget):
    _command: Callable = core.add_combo

    def __init__(
        self,
        items: list[str] = [],
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: str = '',
        popup_align_left: bool = False,
        height_small: bool = False,
        height_regular: bool = False,
        height_large: bool = False,
        height_largest: bool = False,
        no_arrow_button: bool = False,
        no_preview: bool = False,
    ):
        super().__init__(
            items=items,
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            popup_align_left=popup_align_left,
            height_small=height_small,
            height_regular=height_regular,
            height_large=height_large,
            height_largest=height_largest,
            no_arrow_button=no_arrow_button,
            no_preview=no_preview,
        )
        self.items = items
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.popup_align_left = popup_align_left
        self.height_small = height_small
        self.height_regular = height_regular
        self.height_large = height_large
        self.height_largest = height_largest
        self.no_arrow_button = no_arrow_button
        self.no_preview = no_preview


class DatePicker(Widget):
    _command: Callable = core.add_date_picker

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
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: dict = {'month_day':14,'year':20,'month':5},
        level: int = 0,
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
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            level=level,
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
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.level = level


class DragFloat(Widget):
    _command: Callable = core.add_drag_float

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: float = 0.0,
        format: str = '%0.3f',
        speed: float = 1.0,
        min_value: float = 0.0,
        max_value: float = 100.0,
        no_input: bool = False,
        clamped: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragFloatx(Widget):
    _command: Callable = core.add_drag_floatx

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[float] = [0.0,0.0,0.0,0.0],
        size: int = 4,
        format: str = '%0.3f',
        speed: float = 1.0,
        min_value: float = 0.0,
        max_value: float = 100.0,
        no_input: bool = False,
        clamped: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            size=size,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.size = size
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragInt(Widget):
    _command: Callable = core.add_drag_int

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: int = 0,
        format: str = '%d',
        speed: float = 1.0,
        min_value: int = 0,
        max_value: int = 100,
        no_input: bool = False,
        clamped: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragIntx(Widget):
    _command: Callable = core.add_drag_intx

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[int] = [0,0,0,0],
        size: int = 4,
        format: str = '%d',
        speed: float = 1.0,
        min_value: int = 0,
        max_value: int = 100,
        no_input: bool = False,
        clamped: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            size=size,
            format=format,
            speed=speed,
            min_value=min_value,
            max_value=max_value,
            no_input=no_input,
            clamped=clamped,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.size = size
        self.format = format
        self.speed = speed
        self.min_value = min_value
        self.max_value = max_value
        self.no_input = no_input
        self.clamped = clamped


class DragLine(Widget):
    _command: Callable = core.add_drag_line

    def __init__(
        self,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        callback: Callable = None,
        show: bool = True,
        default_value: Any = [0.0,0.0,0.0,0.0],
        color: list[int]=(0,0,0,-255),
        thickness: float = 1.0,
        show_label: bool = True,
        vertical: bool = True,
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            default_value=default_value,
            thickness=thickness,
            show_label=show_label,
            vertical=vertical,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.callback = callback
        self.show = show
        self.default_value = default_value
        self.thickness = thickness
        self.show_label = show_label
        self.vertical = vertical


class DragPoint(Widget):
    _command: Callable = core.add_drag_point

    def __init__(
        self,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        callback: Callable = None,
        show: bool = True,
        default_value: Any = [0.0,0.0,0.0,0.0],
        color: list[int]=(0,0,0,-255),
        thickness: float = 1.0,
        show_label: bool = True,
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            source=source,
            callback=callback,
            show=show,
            default_value=default_value,
            color=color,
            thickness=thickness,
            show_label=show_label,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.callback = callback
        self.show = show
        self.default_value = default_value
        self.thickness = thickness
        self.show_label = show_label


class Dummy(Widget):
    _command: Callable = core.add_dummy

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        show: bool = True,
        pos: list[int] = [],
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos


class DynamicTexture(Widget):
    _command: Callable = core.add_dynamic_texture

    def __init__(
        self,
        height: int,
        default_value: list[float],
        label: str = None,
        parent: int = 0,
    ):
        super().__init__(
            height=height,
            default_value=default_value,
            label=label,
            parent=parent,
        )
        self.height = height
        self.default_value = default_value
        self.label = label
        self.parent = parent


class ErrorSeries(Widget):
    _command: Callable = core.add_error_series

    def __init__(
        self,
        x: list[float],
        y: list[float],
        negative: list[float],
        positive: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        contribute_to_bounds: bool = True,
        horizontal: bool = False,
    ):
        super().__init__(
            x=x,
            y=y,
            negative=negative,
            positive=positive,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
            horizontal=horizontal,
        )
        self.x = x
        self.y = y
        self.negative = negative
        self.positive = positive
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.contribute_to_bounds = contribute_to_bounds
        self.horizontal = horizontal


class FileExtension(Widget):
    _command: Callable = core.add_file_extension

    def __init__(
        self,
        extension: str,
        label: str = None,
        height: int = 0,
        parent: int = 0,
        before: int = 0,
        custom_text: str = '',
        color: list[float] = [-255,0,0,255],
    ):
        super().__init__(
            extension=extension,
            label=label,
            height=height,
            parent=parent,
            before=before,
            custom_text=custom_text,
            color=color,
        )
        self.extension = extension
        self.label = label
        self.height = height
        self.parent = parent
        self.before = before
        self.custom_text = custom_text
        self.color = color


class Font(Widget):
    _command: Callable = core.add_font

    def __init__(
        self,
        file: str,
        size: int,
        label: str = None,
        parent: int = 0,
        default_font: bool = False,
    ):
        super().__init__(
            file=file,
            size=size,
            label=label,
            parent=parent,
            default_font=default_font,
        )
        self.file = file
        self.size = size
        self.label = label
        self.parent = parent
        self.default_font = default_font


class HeatSeries(Widget):
    _command: Callable = core.add_heat_series

    def __init__(
        self,
        x: list[float],
        rows: int,
        cols: int,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        scale_min: float = 0.0,
        scale_max: float = 1.0,
        bounds_min: Any = [0.0,0.0],
        bounds_max: Any = [1.0,1.0],
        format: str = '%0.1f',
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            rows=rows,
            cols=cols,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            scale_min=scale_min,
            scale_max=scale_max,
            bounds_min=bounds_min,
            bounds_max=bounds_max,
            format=format,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.rows = rows
        self.cols = cols
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.scale_min = scale_min
        self.scale_max = scale_max
        self.bounds_min = bounds_min
        self.format = format
        self.contribute_to_bounds = contribute_to_bounds


class HistogramSeries(Widget):
    _command: Callable = core.add_histogram_series

    def __init__(
        self,
        x: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        bins: int = -1,
        bar_scale: float = 1.0,
        min_range: float = 0.0,
        max_range: float = 1.0,
        cumlative: bool = False,
        density: bool = False,
        outliers: bool = True,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            bins=bins,
            bar_scale=bar_scale,
            min_range=min_range,
            max_range=max_range,
            cumlative=cumlative,
            density=density,
            outliers=outliers,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.bins = bins
        self.bar_scale = bar_scale
        self.min_range = min_range
        self.max_range = max_range
        self.cumlative = cumlative
        self.density = density
        self.outliers = outliers
        self.contribute_to_bounds = contribute_to_bounds


class HlineSeries(Widget):
    _command: Callable = core.add_hline_series

    def __init__(
        self,
        x: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.contribute_to_bounds = contribute_to_bounds


class Image(Widget):
    _command: Callable = core.add_image

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        tint_color: list[float] = [255,255,255,255],
        border_color: list[float] = [0,0,0,0],
        uv_min: list[float] = [0.0,0.0],
        uv_max: list[float] = [1.0,1.0],
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            tint_color=tint_color,
            border_color=border_color,
            uv_max=uv_max,
            uv_min=uv_min
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.tint_color = tint_color


class ImageButton(Widget):
    _command: Callable = core.add_image_button

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        frame_padding: int = -1,
        tint_color: list[float] = [255,255,255,255],
        background_color: list[float] = [0,0,0,0],
        uv_min: list[float] = [0.0,0.0],
        uv_max: list[float] = [1.0,1.0],
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            frame_padding=frame_padding,
            tint_color=tint_color,
            background_color=background_color,
            uv_min=uv_min,
            uv_max=uv_max,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.frame_padding = frame_padding
        self.tint_color = tint_color


class ImageSeries(Widget):
    _command: Callable = core.add_image_series

    def __init__(
        self,
        bounds_min: list[float],
        bounds_max: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        uv_min: list[float] = [0.0,0.0],
        uv_max: list[float] = [1.0,1.0],
        tint_color: list[int] = [255,255,255,255],
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            bounds_min=bounds_min,
            bounds_max=bounds_max,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            uv_min=uv_min,
            uv_max=uv_max,
            tint_color=tint_color,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.bounds_min = bounds_min
        self.bounds_max = bounds_max
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.uv_min = uv_min
        self.contribute_to_bounds = contribute_to_bounds


class InputFloat(Widget):
    _command: Callable = core.add_input_float

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: float = 0.0,
        format: str = '%.3f',
        min_value: float = 0.0,
        max_value: float = 100.0,
        step: float = 0.1,
        step_fast: float = 1.0,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.format = format
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.step_fast = step_fast
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputFloatx(Widget):
    _command: Callable = core.add_input_floatx

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[float] = [0.0,0.0,0.0,0.0],
        format: str = '%.3f',
        min_value: float = 0.0,
        max_value: float = 100.0,
        size: int = 4,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            format=format,
            min_value=min_value,
            max_value=max_value,
            size=size,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.format = format
        self.min_value = min_value
        self.max_value = max_value
        self.size = size
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputInt(Widget):
    _command: Callable = core.add_input_int

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[int] = [0,0,0,0],
        min_value: int = 0,
        max_value: int = 100,
        step: int = 1,
        step_fast: int = 100,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            step=step,
            step_fast=step_fast,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.step_fast = step_fast
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputIntx(Widget):
    _command: Callable = core.add_input_intx

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[int] = [0,0,0,0],
        min_value: int = 0,
        max_value: int = 100,
        size: int = 4,
        min_clamped: bool = False,
        max_clamped: bool = False,
        on_enter: bool = False,
        readonly: bool = False,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            size=size,
            min_clamped=min_clamped,
            max_clamped=max_clamped,
            on_enter=on_enter,
            readonly=readonly,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value
        self.size = size
        self.min_clamped = min_clamped
        self.max_clamped = max_clamped
        self.on_enter = on_enter
        self.readonly = readonly


class InputText(Widget):
    _command: Callable = core.add_input_text

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: str = '',
        hint: str = '',
        multiline: bool = False,
        no_spaces: bool = False,
        uppercase: bool = False,
        tab_input: bool = False,
        decimal: bool = False,
        hexadecimal: bool = False,
        readonly: bool = False,
        password: bool = False,
        scientific: bool = False,
        on_enter: bool = False,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            hint=hint,
            multiline=multiline,
            no_spaces=no_spaces,
            uppercase=uppercase,
            tab_input=tab_input,
            decimal=decimal,
            hexadecimal=hexadecimal,
            readonly=readonly,
            password=password,
            scientific=scientific,
            on_enter=on_enter,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.hint = hint
        self.multiline = multiline
        self.no_spaces = no_spaces
        self.uppercase = uppercase
        self.tab_input = tab_input
        self.decimal = decimal
        self.hexadecimal = hexadecimal
        self.readonly = readonly
        self.password = password
        self.scientific = scientific
        self.on_enter = on_enter


class KnobFloat(Widget):
    _command: Callable = core.add_knob_float

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: float = 0.0,
        min_value: float = 0.0,
        max_value: float = 100.0,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value


class LineSeries(Widget):
    _command: Callable = core.add_line_series

    def __init__(
        self,
        x: list[float],
        y: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.contribute_to_bounds = contribute_to_bounds


class Listbox(Widget):
    _command: Callable = core.add_listbox

    def __init__(
        self,
        items: list[str] = [],
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: str = '',
        num_items: int = 3,
    ):
        super().__init__(
            items=items,
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            num_items=num_items,
        )
        self.items = items
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.num_items = num_items


class LoadingIndicator(Widget):
    _command: Callable = core.add_loading_indicator

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        show: bool = True,
        pos: list[int] = [],
        style: int = 0,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            style=style,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos
        self.style = style


class PieSeries(Widget):
    _command: Callable = core.add_pie_series

    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        values: list[float],
        labels: list[str],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        format: str = '%0.2f',
        angle: float = 90.0,
        normalize: bool = False,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y=y,
            radius=radius,
            values=values,
            labels=labels,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            format=format,
            angle=angle,
            normalize=normalize,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y = y
        self.radius = radius
        self.values = values
        self.labels = labels
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.format = format
        self.angle = angle
        self.normalize = normalize
        self.contribute_to_bounds = contribute_to_bounds


class ProgressBar(Widget):
    _command: Callable = core.add_progress_bar

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        overlay: str = '',
        default_value: float = 0.0,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            overlay=overlay,
            default_value=default_value,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.overlay = overlay
        self.default_value = default_value


class RadioButton(Widget):
    _command: Callable = core.add_radio_button

    def __init__(
        self,
        items: int = [],
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: str = '',
        horizontal: bool = False,
    ):
        super().__init__(
            items=items,
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            horizontal=horizontal,
        )
        self.items = items
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.horizontal = horizontal


class SameLine(Widget):
    _command: Callable = core.add_same_line

    def __init__(
        self,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        show: bool = True,
        xoffset: float = 0.0,
        spacing: float = -1.0,
    ):
        super().__init__(
            label=label,
            parent=parent,
            before=before,
            show=show,
            xoffset=xoffset,
            spacing=spacing,
        )
        self.label = label
        self.parent = parent
        self.before = before
        self.show = show
        self.xoffset = xoffset
        self.spacing = spacing


class ScatterSeries(Widget):
    _command: Callable = core.add_scatter_series

    def __init__(
        self,
        x: list[float],
        y: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.contribute_to_bounds = contribute_to_bounds


class Selectable(Widget):
    _command: Callable = core.add_selectable

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: bool = False,
        span_columns: bool = False,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            span_columns=span_columns,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.span_columns = span_columns


class Separator(Widget):
    _command: Callable = core.add_separator

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        show: bool = True,
        pos: list[int] = [],
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos


class ShadeSeries(Widget):
    _command: Callable = core.add_shade_series

    def __init__(
        self,
        x: list[float],
        y1: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        y2: Any = [],
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y1=y1,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            y2=y2,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y1 = y1
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.y2 = y2
        self.contribute_to_bounds = contribute_to_bounds


class SimplePlot(Widget):
    _command: Callable = core.add_simple_plot

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        show: bool = True,
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[float] = [],
        overlay: str = '',
        histogram: bool = False,
        autosize: bool = True,
        min_scale: float = 0.0,
        max_scale: float = 0.0,
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            overlay=overlay,
            histogram=histogram,
            autosize=autosize,
            min_scale=min_scale,
            max_scale=max_scale,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.show = show
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.overlay = overlay
        self.histogram = histogram
        self.autosize = autosize
        self.min_scale = min_scale
        self.max_scale = max_scale


class SliderFloat(Widget):
    _command: Callable = core.add_slider_float

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: float = 0.0,
        vertical: bool = False,
        no_input: bool = False,
        clamped: bool = False,
        min_value: float = 0.0,
        max_value: float = 100.0,
        format: str = '%.3f',
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.vertical = vertical
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderFloatx(Widget):
    _command: Callable = core.add_slider_floatx

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[float] = [0.0,0.0,0.0,0.0],
        size: int = 4,
        no_input: bool = False,
        clamped: bool = False,
        min_value: float = 0.0,
        max_value: float = 100.0,
        format: str = '%.3f',
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            size=size,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.size = size
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderInt(Widget):
    _command: Callable = core.add_slider_int

    def __init__(
        self,
        label: str = None,
        height: int = 0,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: int = 0,
        vertical: bool = False,
        no_input: bool = False,
        clamped: bool = False,
        min_value: int = 0,
        max_value: int = 100,
        format: str = '%d',
    ):
        super().__init__(
            label=label,
            height=height,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            vertical=vertical,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
        )
        self.label = label
        self.height = height
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.vertical = vertical
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class SliderIntx(Widget):
    _command: Callable = core.add_slider_intx

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        payload_type: str = '$$DPG_PAYLOAD',
        callback: Callable = None,
        drag_callback: Callable = None,
        drop_callback: Callable = None,
        user_data: Any = None,
        show: bool = True,
        enabled: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: list[int] = [0,0,0,0],
        size: int = 4,
        no_input: bool = False,
        clamped: bool = False,
        min_value: int = 0,
        max_value: int = 100,
        format: str = '%d',
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            callback=callback,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            user_data=user_data,
            show=show,
            enabled=enabled,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            size=size,
            no_input=no_input,
            clamped=clamped,
            min_value=min_value,
            max_value=max_value,
            format=format,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.payload_type = payload_type
        self.callback = callback
        self.drag_callback = drag_callback
        self.drop_callback = drop_callback
        self.user_data = user_data
        self.show = show
        self.enabled = enabled
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.size = size
        self.no_input = no_input
        self.clamped = clamped
        self.min_value = min_value
        self.max_value = max_value
        self.format = format


class Spacing(Widget):
    _command: Callable = core.add_spacing

    def __init__(
        self,
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        show: bool = True,
        pos: list[int] = [],
        count: int = 1,
    ):
        super().__init__(
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            pos=pos,
            count=count,
        )
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.show = show
        self.pos = pos
        self.count = count


class StairSeries(Widget):
    _command: Callable = core.add_stair_series

    def __init__(
        self,
        x: list[float],
        y: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.contribute_to_bounds = contribute_to_bounds


class StaticTexture(Widget):
    _command: Callable = core.add_static_texture

    def __init__(
        self,
        height: int,
        default_value: list[float],
        label: str = None,
        parent: int = 0,
        file: str = '',
    ):
        super().__init__(
            height=height,
            default_value=default_value,
            label=label,
            parent=parent,
            file=file,
        )
        self.height = height
        self.default_value = default_value
        self.label = label
        self.parent = parent
        self.file = file


class StemSeries(Widget):
    _command: Callable = core.add_stem_series

    def __init__(
        self,
        x: list[float],
        y: list[float],
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.y = y
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.contribute_to_bounds = contribute_to_bounds


class Text(Widget):
    _command: Callable = core.add_text

    def __init__(
        self,
        default_value: str = '',
        label: str = None,
        indent: int = -1,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        pos: list[int] = [],
        filter_key: str = '',
        tracked: bool = False,
        track_offset: float = 0.5,
        wrap: int = -1,
        bullet: bool = False,
        color: list[float] = [-1,-1,-1,-1],
        show_label: bool = False,
    ):
        super().__init__(
            default_value=default_value,
            label=label,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            wrap=wrap,
            bullet=bullet,
            color=color,
            show_label=show_label,
        )
        self.default_value = default_value
        self.label = label
        self.indent = indent
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.pos = pos
        self.filter_key = filter_key
        self.tracked = tracked
        self.track_offset = track_offset
        self.wrap = wrap
        self.bullet = bullet
        self.color = color
        self.show_label = show_label


class TextPoint(Widget):
    _command: Callable = core.add_text_point

    def __init__(
        self,
        x: float,
        y: float,
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        x_offset: int = ...,
        y_offset: int = ...,
        contribute_to_bounds: bool = True,
        vertical: bool = False,
    ):
        super().__init__(
            x=x,
            y=y,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            x_offset=x_offset,
            y_offset=y_offset,
            contribute_to_bounds=contribute_to_bounds,
            vertical=vertical,
        )
        self.x = x
        self.y = y
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.contribute_to_bounds = contribute_to_bounds
        self.vertical = vertical


class TimePicker(Widget):
    _command: Callable = core.add_time_picker

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
        tracked: bool = False,
        track_offset: float = 0.5,
        default_value: dict = {'hour':14,'min':32,'sec':23},
        hour24: bool = False,
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
            tracked=tracked,
            track_offset=track_offset,
            default_value=default_value,
            hour24=hour24,
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
        self.tracked = tracked
        self.track_offset = track_offset
        self.default_value = default_value
        self.hour24 = hour24


class VlineSeries(Widget):
    _command: Callable = core.add_vline_series

    def __init__(
        self,
        x: list[float],
        label: str = None,
        parent: int = 0,
        before: int = 0,
        source: int = 0,
        show: bool = True,
        contribute_to_bounds: bool = True,
    ):
        super().__init__(
            x=x,
            label=label,
            parent=parent,
            before=before,
            source=source,
            show=show,
            contribute_to_bounds=contribute_to_bounds,
        )
        self.x = x
        self.label = label
        self.parent = parent
        self.before = before
        self.source = source
        self.show = show
        self.contribute_to_bounds = contribute_to_bounds
