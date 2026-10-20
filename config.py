from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension
import subprocess

modkey = "mod4"
mod = "mod1"
terminal = guess_terminal()
#dmenu_cmd="/home/em0n/.config/suckless/dmenu/dmenu_run -l 10 -nb '#0f1012' -nf '#ffffff' -sb '#232529'"
rofi_drun="rofi -show drun"
rofi_window="rofi -show window"
rofi_greenclip="rofi -modi 'clipboard:greenclip print' -show clipboard"

keys = [

    #############################
    ##### SWITCH BETWEEN WINDOWS
    #############################
    Key([mod], "k", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "e", lazy.layout.next(), desc="Move window focus to other window"),


    #############################
    ##### COLUMN
    #############################
    Key([modkey, "shift"], "h", lazy.layout.grow_left()),
    Key([modkey, "shift"], "l", lazy.layout.grow_right()),
    Key([modkey, "shift"], "j", lazy.layout.swap_column_left()),
    Key([modkey, "shift"], "k", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "p", lazy.layout.toggle_split()),

    #############################
    ##### MONADTALL
    #############################
    Key([mod], "h", lazy.layout.shrink_main()),
    Key([mod], "l", lazy.layout.grow_main()),
    Key([mod], "m", lazy.layout.swap_main()),


    #############################
    ##### MONADWIDE
    #############################
    Key([mod], "n", lazy.layout.grow()),
    Key([modkey], "k", lazy.layout.up()),
    Key([modkey], "j", lazy.layout.down()),
    Key([modkey], "h", lazy.layout.left()),
    Key([modkey], "l", lazy.layout.right()),
    Key([mod, "shift"], "n", lazy.layout.shrink()),
    Key([mod, "shift"], "u", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "d", lazy.layout.shuffle_down()),

    #############################
    ###### Floating
    ############################
    #Key([mod], "k", lazy.layout.next()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    #############################
    ####### SPAWN APPLICATIONS
    #############################
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #Key([mod], "p", lazy.spawn(dmenu_cmd)),
    Key([mod], "p", lazy.spawn(rofi_drun)),
    Key([mod], "c", lazy.spawn(rofi_greenclip)),
    Key([mod, "shift"], "w", lazy.spawn(rofi_window)),
    Key([mod, "shift"], "e", lazy.spawn("thunar")),
    Key([mod, "shift"], "x", lazy.spawn("flameshot gui")),
    Key([mod, "shift"], "p", lazy.spawn("redshift -O 6000")),
    Key([mod, "shift"], "z", lazy.spawn("redshift -x")),
    Key([mod, "shift"], "r", lazy.spawn("/home/em0n/.config/qtile/rice.sh"), desc="Run linux ricing script"),


    #############################
    ####### OTHERS
    ############################
    Key([mod, "shift"], "m", lazy.hide_show_bar(), desc="Hide qtile bar for all layouts"),
    #Key([mod, "shift"], "m", lazy.window.toggle_fullscreen(), desc="Hide qtile bar for current layout"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "d", lazy.next_layout()),
    Key([mod], "i", lazy.prev_layout()),

]

# WAYLAND KEYS
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

#groups = [
#    Group('1', label=""),
#    Group('2', label=""),
#    Group('3', label=" "),
#    Group('4', label=""),
#    Group('5', label=""),
#    Group('6', label=""),
#    Group('7', label="󰠰 "),
#    Group('8', label=""),
#    Group('9', label=""),    
#]

#groups = [
#    Group('1', label=""),
#    Group('2', label=""),
#    Group('3', label=""),
#    Group('4', label=""),
#    Group('5', label=""),
#    Group('6', label=""),
#    Group('7', label=""),
#    Group('8', label=""),
#    Group('9', label=""),
#]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),

            Key([mod], "space", lazy.group["scratchpad"].dropdown_toggle("term")),
            Key([mod, "shift"], "space", lazy.group["scratchpad"].dropdown_toggle("xnote")),
        ]
    )

groups.append(
    ScratchPad("scratchpad", [
        DropDown("term", terminal, opacity=0.9, height=0.4, width=0.80),
        DropDown("xnote", "python3 /home/em0n/Projects/Desktop-apps/Xnote/xnote.py", opacity=1, height=0.6, width=0.58, x=0.21, y=0.2),
    ]),
)

border = "#6b7275"
#border = "#5a6063"
bordermargin = 0

layouts = [
    layout.MonadTall(
        border_focus=border,
        border_normal='#141414',
        border_width=1,
        single_border_width=1,
        single_margin=bordermargin,
        margin = bordermargin,
        max_ratio = 0.90,
        name = "[ ]=",
    ),
    layout.MonadWide(
        border_focus=border,
        border_normal='#141414',
        border_width=1,
        single_border_width=1,
        margin=bordermargin,
        single_margin=bordermargin,
    ),
    layout.Max(
        border_focus=border,
        border_normal='#141414',
        border_width=1,
        margin = bordermargin,
    ),
    layout.Columns(
        border_focus=border,
        border_normal='#141414',
        border_normal_stack='#141414',
        border_on_single=True,
        border_width=1,
        margin=[2, 2, 2, 2],
        margin_on_single=[100, 120, 100, 120],
        insert_position=1,
        num_columns=3,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=0,
)
extension_defaults = widget_defaults.copy()

win_sep = '#2f3a40'
win_gap = 15
fsize = 14
my_foreground = "#bababa"
text_fg = "#000000"
my_font = "JetBrainsMono Nerd Font Bold"
ac_col = "#8f6f78"

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    font=my_font,
                    highlight_method="block", 
                    this_current_screen_border="#8c414b", 
                    block_highlight_text_color="#f0f0f0",
                    inactive="#999999",
                    hide_unused=True,
                    fontsize=13,
                    padding_x=5,
                    padding_y=2,
                ),

                widget.Sep(
                    linewidth = 1,
                    padding = win_gap,
                    foreground = win_sep,
                ),
                
                widget.CurrentLayout(
                    font = my_font,
                    fontsize = fsize,
                    foreground = '#8c9296',
                    center_aligned = True,
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = win_gap,
                    foreground = win_sep,
                ),
                
                widget.WindowName(
                    font = my_font,
                    fontsize = fsize,
                    foreground = '#8c9296',
                    format = "{name}",
                    center_aligned = True,
                    max_chars = 50,
                ),
                widget.TextBox(
                    text = "󰤨",
                    fontsize = 13,
                    foreground = "#8bb1c7",
                    padding = 10
                ),
                widget.Net(
                    font=my_font,
                    fontsize = fsize,
                    format='all: {down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix} |',
                    update_interval=30,
                    foreground=my_foreground,
                    background = text_fg,
                ),
                widget.TextBox(
                    text = "",
                    fontsize = 13,
                    foreground = "#b07b7b",
                    padding = 10
                ),
                widget.CPU(
                    font = my_font,
                    fontsize = fsize,
                    foreground = my_foreground,
                    format = 'CPU: {load_percent}% |', 
                    background = text_fg,
                ),
                widget.TextBox(
                    text = "",
                    fontsize = 13,
                    foreground = "#977bb0",
                    padding = 10
                ),
                widget.Memory(
                    font = my_font,
                    fontsize = fsize,
                    foreground = my_foreground,
                    format = 'MEMORY: {MemUsed:.0f}{mm} |',
                    background = text_fg,
                ),
                widget.TextBox(
                    text = "󱑂",
                    fontsize = 14,
                    foreground = "#80b07b",
                    padding = 10
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p ",
                    font = my_font,
                    fontsize = fsize,
                    foreground = my_foreground,
                    center_aligned = True,
                    background = text_fg,
                ),
                widget.Systray(
                    icon_size = 18,
                    padding = 4,
                    background = "#000000",
                ),

            ],
            28,
            background = text_fg,
            margin = [0, 0, 0, 0],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True # CHNAGED True to False
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=border,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

def autostart():
    subprocess.call(["/home/em0n/.config/qtile/autostart.sh"])

autostart()
