from modules.groups import groups
from modules.hooks import *
from modules.keys import keys, mod
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import screens
from modules.widgets import *

import os
import subprocess

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"