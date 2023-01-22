# __                           _   _ _                     __     #
# \ \                     __ _| |_(_) | ___                \ \    #
#  \ \ _____ _____ _____ / _` | __| | |/ _ \_____ _____ ____\ \   #
#   \ \_____|_____|_____| (_| | |_| | |  __/_____|_____|_____\ \  #
#    \_\                 \__, |\__|_|_|\___|                  \_\ #
#                           |_|                                   #

# ---imports--- #
from libqtile import bar, layout, hook
from libqtile.config import Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os, subprocess

# ---environment--- #
HOME = os.getenv("HOME")
CONFIG = f"{os.getenv('XDG_CONFIG_HOME')}/qtile"

# ---hardware buttons--- #
POWOFF = "XF86PowerOff"
VOLUP = "XF86AudioRaiseVolume"
VOLDN = "XF86AudioLowerVolume"
VOLMUTE = "XF86AudioMute"
SUSPEND = "XF86Sleep"

# ---mod keys--- #
CTRL = "control"
MOD = "mod4"
META = "mod1"
RTRN = "Return"
SHIFT = "shift"
TAB = "Tab"
LEFTMB = "Button1"
MIDMB = "Button2"
RIGHTMB = "Button3"

# ---default launchers--- #
TERM = "kitty"
WEB_BROWSER = "librewolf"
FILE_BROWSER = f"{TERM} -- ranger"
SCRN_LOCK = f"{CONFIG}/scripts/lock.sh"
SESS_CTRL = f"sh {CONFIG}/scripts/session_options.sh"

# on startup
@hook.subscribe.startup_once
def autostart():
    subprocess.run(f"{CONFIG}/scripts/startup.sh")


# ---screens--- #
screens = [Screen(top=bar.Gap(26))]

# ---keys--- #
keys = [
    # move focus
    Key([MOD], "Left", lazy.layout.left(), desc="focus left"),
    Key([MOD], "Right", lazy.layout.right(), desc="focus right"),
    Key([MOD], "Down", lazy.layout.down(), desc="focus down"),
    Key([MOD], "Up", lazy.layout.up(), desc="focus up"),
    # control window
    Key([MOD, SHIFT], "Left", lazy.layout.shuffle_left(), desc="move window left"),
    Key([MOD, SHIFT], "Right", lazy.layout.shuffle_right(), desc="move window right"),
    Key([MOD, SHIFT], "Down", lazy.layout.shuffle_down(), desc="move window down"),
    Key([MOD, SHIFT], "Up", lazy.layout.shuffle_up(), desc="move window up"),
    Key([MOD], "q", lazy.window.kill(), desc="kill window"),
    # modify window size
    Key([MOD], "h", lazy.layout.grow_left(), desc="grow window left"),
    Key([MOD], "l", lazy.layout.grow_right(), desc="grow window right"),
    Key([MOD], "j", lazy.layout.grow_down(), desc="grow window down"),
    Key([MOD], "k", lazy.layout.grow_up(), desc="grow window up"),
    Key([MOD, CTRL], "n", lazy.layout.normalize(), desc="reset all window sizes"),
    # launchers
    Key([MOD], "space", lazy.spawn("rofi -show drun"), desc="show drun"),
    Key([MOD], TAB, lazy.spawn("rofi -show window"), desc="show active windows"),
    Key([MOD], "Print", lazy.spawn("flameshot gui"), desc="launch flameshot gui"),
    Key([], "Print", lazy.spawn(f"flameshot screen -r -p {HOME}/pictures/screenshots")),
    Key([MOD], RTRN, lazy.spawn(TERM), desc="launch terminal"),
    Key([MOD], "f", lazy.spawn(FILE_BROWSER), desc="launch file browser"),
    Key([MOD], "b", lazy.spawn(WEB_BROWSER), desc="launch web browser"),
    # toggle floating
    Key([MOD], "t", lazy.window.toggle_floating(), desc="toggle floating"),
    # hardware keys control
    Key(
        [],
        POWOFF,
        lazy.spawn(SESS_CTRL),
        desc="session options",
    ),
    Key(
        [],
        SUSPEND,
        lazy.spawn(f"{SESS_CTRL} suspend"),
        desc="lock screen and suspend",
    ),
    Key([], VOLUP, lazy.spawn("pamixer -i 10"), desc="raise volume by 10%"),
    Key([], VOLDN, lazy.spawn("pamixer -d 10"), desc="lower volume by 10%"),
    Key([], VOLMUTE, lazy.spawn("pamixer -t"), desc="mute/unmute volume"),
    # session control
    Key(
        [CTRL],
        "l",
        lazy.spawn(SCRN_LOCK),
        desc="lock screen",
    ),
    Key(
        [CTRL, META],
        "Delete",
        lazy.spawn(f"{SESS_CTRL} log-out"),
        desc="session options",
    ),
    Key(
        [CTRL, META],
        "r",
        lazy.spawn(f"sh {CONFIG}/scripts/restart.sh"),
        desc="restart session",
    ),
]

# ---groups--- #
groups = [Group(i) for i in "1234567890"]
for i in groups:
    keys.extend(
        [
            # mod + group number --> switch to group number
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"switch to group {i.name}",
            ),
            # mod + shift + group number --> move focused window to group number
            Key(
                [MOD, SHIFT],
                i.name,
                lazy.window.togroup(i.name),
                desc=f"move focused window to group {i.name}",
            ),
        ]
    )

# ---layouts--- #
layouts = [
    layout.Columns(
        autosplit=True,
        border_focus="#69ff94",
        border_normal="#ffffa5",
        border_width=3,
        fair=False,
        grow_amount=5,
        margin=2,
        num_columns=2,
    ),
]

# ---manage floating windows--- #
# mouse controls
mouse = [
    # mod + left mouse button --> move floating window
    Drag(
        [MOD],
        LEFTMB,
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    # mod + right mouse button --> resize floating window
    Drag([MOD], RIGHTMB, lazy.window.set_size_floating(), start=lazy.window.get_size()),
]
# default floating layout
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)

# ---general settings--- #
# generate group binding hotkeys
dgroups_key_binder = None
# send certain windows to specific group
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
# cursor follows focus
cursor_warp = False
auto_fullscreen = True
# allow windows to be focused on `_NET_ACTIVATE_WINDOW` message
focus_on_window_activation = "smart"
reconfigure_screens = True
# allow windows to be minimized if not focused
auto_minimize = True
# fuck java
wmname = "LG3D"
