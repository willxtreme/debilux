from libqtile import layout
from libqtile.config import Match

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "#96CDFB",
    "border_normal": "#1E1D2F",
}
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(),
    layout.Floating(
        border_focus="#6E6C7E",
        border_normal="#1E1D2F",
        border_width=4,
    ),
]

floating_layout = layout.Floating(
    border_focus="#89DCEB",
    border_normal="#1E1D2F",
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