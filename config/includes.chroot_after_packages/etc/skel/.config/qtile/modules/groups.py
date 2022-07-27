from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from .keys import keys, mod

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