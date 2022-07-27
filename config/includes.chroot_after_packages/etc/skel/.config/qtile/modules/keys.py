from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "alacritty"
browser = "brave-browser"
forcequit = "xkill"
volume = "alacritty -e alsamixer"
filemanager = "pcmanfm"
editor = "mousepad"
mediaplayer = "vlc"
upgrade = "alacritty --hold -e sudo debilux_upgrade"

keys = [
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "w", lazy.spawn(browser)),
    Key([mod], "u", lazy.spawn(upgrade)),
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