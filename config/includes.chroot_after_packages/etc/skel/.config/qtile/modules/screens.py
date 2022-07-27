from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from libqtile import qtile
import os

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="  ",
                    background="#1E1D2F",
                    foreground="#d9e0ee",
                    padding=0,
                    fontsize=20,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show drun")}
                ),
                widget.Sep(
                    foreground="#6E6C7E",
                    line_width=9,
                    size_percent=70,
                ),
                widget.GroupBox(
                    fontsize=18,
                    active="#89DCEB",
                    inactive="#6E6C7E",
                    foreground="#89DCEB",
                    rounded=False,
                    borderwidth=2,
                    margin=4,
                    highlight_method="line",
                    highlight_color="#1E1D2F",
                    other_screen_border="#6E6C7E",
                    other_current_screen_border="#89DCEB",
                    this_current_screen_border="#89DCEB",
                    this_screen_border="#6E6C7E",
                ),
                widget.Sep(
                    foreground="#6E6C7E",
                    line_width=9,
                    size_percent=70,
                ),
                widget.CurrentLayout(
                    background="#1E1D2F",
                    foreground="#d9e0ee",
                ),
                widget.Sep(
                    foreground="#6E6C7E",
                    line_width=9,
                    size_percent=70,
                ),
                widget.WindowName(foreground="#d9e0ee"),
                widget.Spacer(length=100),
                widget.Prompt(),
                widget.Systray(icon_size=24),
                widget.Sep(
                    foreground="#6E6C7E",
                    line_width=9,
                    size_percent=70,
                ),
                widget.TextBox(
                    text="  ",
                    background="#1E1D2F",
                    foreground="#96CDFB",
                    padding=0,
                    fontsize=17,
                ),
                widget.Clock(
                    background="#1E1D2F",
                    foreground="#d9e0ee",
                    format="%b %d - %I:%M%p",
                ),
                widget.Sep(
                    foreground="#6E6C7E",
                    line_width=9,
                    size_percent=70,
                ),
                widget.QuickExit(
                    background="#1E1D2F",
                    foreground="#F28FAD",
                    default_text=" ",
                ),
            ],
            30,
            background="#1E1D2F",
            opacity=20,
            margin=[10, 10, 5, 10],
        ),
    ),
]
