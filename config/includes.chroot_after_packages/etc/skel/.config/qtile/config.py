# Imports
import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# Apps
mod = "mod4"
terminal = "alacritty"
browser = "brave-browser"
forcequit = "xkill"
volume = "alacritty -e alsamixer"
filemanager = "pcmanfm"
editor = "mousepad"
mediaplayer = "vlc"

# Colors
bg = "#1E1D2F"
blue = "#96CDFB"
cyan = "#89DCEB"
fg = "#d9e0ee"
gray = "#6E6C7E"
magenta = "#F5C2E7"
red = "#F28FAD"
yellow = "#FAE3B0"

# Keys
keys = [
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "w", lazy.spawn(browser)),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "q", lazy.spawn(forcequit)),
    Key([mod], "v", lazy.spawn(volume)),
    Key([mod], "e", lazy.spawn(filemanager)),
    Key([mod], "t", lazy.spawn(editor)),
    Key([mod], "m", lazy.spawn(mediaplayer)),
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "control"], "space", lazy.layout.flip()),
    Key([mod, "shift"], "space", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "c", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.reload_config()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset -q Master,0 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset -q Master,0 5%+")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "Print", lazy.spawn("scrot")),
]

# Groups
groups = [Group(i) for i in ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]]
group_hotkeys = "1234567890"
for i, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            Key(
                [mod],
                k,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

# Layouts
layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": blue,
    "border_normal": bg,
}
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(),
    layout.Floating(
        border_focus=gray,
        border_normal=bg,
        border_width=4,
    ),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=18,
    padding=9,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="  ",
                    background=bg,
                    foreground=fg,
                    padding=0,
                    fontsize=20,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show drun")}
                ),
                widget.Sep(
                    foreground=gray,
                    line_width=9,
                    size_percent=70,
                ),
                widget.GroupBox(
                    fontsize=18,
                    active=cyan,
                    inactive=gray,
                    foreground=cyan,
                    rounded=False,
                    borderwidth=2,
                    margin=4,
                    highlight_method="line",
                    highlight_color=bg,
                    other_screen_border=gray,
                    other_current_screen_border=cyan,
                    this_current_screen_border=cyan,
                    this_screen_border=gray,
                ),
                widget.Sep(
                    foreground=gray,
                    line_width=9,
                    size_percent=70,
                ),
                widget.CurrentLayout(
                    background=bg,
                    foreground=fg,
                ),
                widget.Sep(
                    foreground=gray,
                    line_width=9,
                    size_percent=70,
                ),
                widget.WindowName(foreground=fg),
                widget.Spacer(length=100),
                widget.Prompt(),
                widget.Systray(icon_size=24),
                widget.Sep(
                    foreground=gray,
                    line_width=9,
                    size_percent=70,
                ),
                widget.TextBox(
                    text="  ",
                    background=bg,
                    foreground=blue,
                    padding=0,
                    fontsize=17,
                ),
                widget.Clock(
                    background=bg,
                    foreground=fg,
                    format="%b %d - %I:%M%p",
                ),
                widget.Sep(
                    foreground=gray,
                    line_width=9,
                    size_percent=70,
                ),
                widget.QuickExit(
                    background=bg,
                    foreground=red,
                    default_text=" ",
                ),
            ],
            30,
            background=bg,
            opacity=20,
            margin=[10, 10, 5, 10],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=cyan,
    border_normal=bg,
    border_width=2,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])


wmname = "LG3D"
