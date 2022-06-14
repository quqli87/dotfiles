#
#   __ _  __ _| |
#  / _` |/ _` | |
# | (_| | (_| | |
#  \__, |\__, |_|
#     |_|   |_|



# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2011, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

# from libqtile import bar, layout, widget
# from libqtile.config import Click, Drag, Group, Key, Match, Screen
# from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.utils import describe_attributes
from libqtile.widget import Spacer
              
colours = [
    '#ffffff',
    '#000000',
    '#ddffff',
    '#5F5FAF',
    '#0000ff',
    '#00ffff',
    ]


mod = "mod4"
#mod = "mod4"
#mod1 = "control"
#terminal = guess_terminal()
#terminal = 'urxvt'
terminal = 'alacritty'
code = 'codium'


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)
main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

keys = [


    #hotkeys keybindings keybinds shortcuts
    #Key([mod], "d", lazy.spawn("/usr/bin/dmenu_run")),
    #Key([mod], "d", lazy.spawn("dmenu_run")),
    Key([mod], "c", lazy.spawn(code)),
    Key([mod], "b", lazy.spawn("brave")),
    Key([mod], "t", lazy.spawn(terminal)),
    #Key([mod], "t", lazy.spawn(terminal)),
    Key([mod], "Return", lazy.spawn('urxvt'), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("thunar")),
    #Key([mod], "z", lazy.spawn("urxvt -e ranger")),
    #Key([mod], "e", qtile.cmd_spawn("urxvt -e ranger"),
    Key([mod], "n", lazy.spawn('Notepadqq')),
    Key([mod, "shift"], "Up", lazy.spawn("xbacklight -inc 2.5"), desc="Increment brightness"),
    Key([mod, "shift"], "Down", lazy.spawn("xbacklight -dec 2.5"), desc="Decrement brightness"),
    Key([mod, "shift"], "f",lazy.spawn("rofi -show run")),
    Key([mod, "shift"], "w",lazy.spawn("rofi -show ")),
    Key([mod, "shift"], "d",lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "s",lazy.spawn("flameshot gui")),
    Key([mod, "shift"], "x",lazy.spawn('betterlockscreen -l blur')),


    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # #Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd()),

# CHANGE FOCUS

Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    #Key([mod], "Left", lazy.layout.left()),
    #Key([mod], "Right", lazy.layout.right()),

# RESIZE UP, DOWN, LEFT, RIGHT
  
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),

    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
   
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),

    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "Return", lazy.layout.flip()),

#FLIP LAYOUT FOR BSP
    Key([mod, "shift"], "k", lazy.layout.flip_up()),
    Key([mod, "shift"], "j", lazy.layout.flip_down()),
    Key([mod, "shift"], "l", lazy.layout.flip_right()),
    Key([mod, "shift"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
#     Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
#     Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
#     Key([mod, "shift"], "Left", lazy.layout.swap_left()),
#     Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    
]

#######         mousecallbacks
#### def open_dmenu(qtile):
    ###qtile.cmd.spawn('urxvt htop')
def open_pacman(qtile):
    qtile.cmd_spawn('urxvt -e sudo pacman -Syu')

#g_symbols = '☿♀♁♂♃♄⛢♆'
#g_symbols = '的是不了在人有我他'
groups=[]
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
# group_labels = ['あ','い','う','え','お','か','き','く','け','人',]
group_labels = ['不','了','人','え','之','大','个','小','中','从',]
group_layouts = ["MonadTall", "MonadTall","MonadTall", "MonadTall","MonadTall", "MonadTall","MonadTall", "MonadTall","MonadTall", "MonadTall",]
# group_layouts = ["Columns","Matrix","MonadTall","MonadWide","Columns","Matrix","MonadTall","MonadWid1e",["Columns","Matrix",]
    # layout.Columns(border_focus_stack='#00005a',border_focus= colours[3]),
    #layout.Max(border_focus_stack='#00005a',border_focus=colour[1]),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(border_focus_stack='#00005a', border_focus=colours[3]),
    # layout.MonadTall(border_focus_stack='#00005a', border_focus=colours[3]),
    # layout.MonadWide(border_focus_stack='#00005a', border_focus=colours[3]),
    # layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    # layout.VerticalTile(),
    #layout.Zoomy(),

#g_symbols = 'あいうえおかきくけ'
#g_symbols = '的是不了在人有我他'
# groups = [Group(name) for name in g_symbols]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            # layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Right", lazy.screen.next_group()),
        Key([mod], "Left", lazy.screen.prev_group()),
       # Key(["mod1", "shift"], "Tab", lazy.screen.next_group()),
       # Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])
def init_layout_theme():
    return {"margin":6,
            "border_width":1,
            "border_focus": colours[3],
            "border_normal": colours[5]
            }

layout_theme = init_layout_theme()
layouts = [
    layout.Max(**layout_theme),
    layout.MonadTall(margin=6, border_width=1, border_focus=colours[3], border_normal="#550055"),
    layout.MonadWide(margin=6, border_width=1, border_focus=colours[3], border_normal="#4c566a"),
    layout.Matrix(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.RatioTile(**layout_theme)
]
# for g in groups:
#     keys.extend([
#         Key([mod], str(g_symbols.index(g.name) + 1),
#             lazy.group[g.name].toscreen()),
#         Key([mod, 'control'], str(g_symbols.index(g.name) + 1),
#             lazy.window.togroup(g.name, switch_group=False)),
#         Key([mod, 'shift'], str(g_symbols.index(g.name) + 1),
#             lazy.window.togroup(g.name, switch_group=True)),
#     ])

# groups2 = [Group(i) for i in "0"]

# for i in groups2:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),

#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])



widget_defaults = dict(
    #font='sans',
    font='UbuntuMono Nerd Font',
    fontsize=12,
    padding=0,
    #background = colours[0],
    #background = colours[0],
    #background = colours[1],)
    #background = '#000000')
    )
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.Spacer(length=33, background="#00000000"),
                #widget.CurrentLayout(),
                widget.GroupBox(font='scientifica', highlight_method='text',
                     #highlight_color['#000000','#282892']],
                     #highlight_color[colours[1], colours[2]],
                     margin_y =3,
                     margin_x =2, 
                     #inactive=colours[4],
                     active=colours[4],
                     foreground=colours[1],
                     background=colours[1],
                     ##hide_unused=True,
                     #border='#ff3333',
                     #block_highlight_text_color='#282893',
                     #block_highlight_text_color=colours[2],
                     #highlight_color=colours[0], foreground = colours[2],
                     #background = colours[3],
                                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ffd2c5", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CheckUpdates(
                    colour_no_updates =colours[0],
                    colour_have_updates = colours[4],
                    update_interval = 300
                       ),
                widget.TextBox(
                         text='\uE0B2',
                #                   #text='❰',
                #                   #text='◀',
                #                   text='🠴',
                         background = colours[1],
                         foreground = colours[3],
                #                   margin_y=19,
                                   padding=0,
                                   fontsize=17
                                   ),
 
#widget.Clipboard(),
                #widget.Backlight(),
                #   widget.Textbox(
                #       text='\uE0B2',
                #             background = colours[1],
                #             frontground = colours[3],
                #             fontsize=13
                #             ),
                widget.Systray(
                         background = colours[3],
                         ground = colours[3],
                         icon_size=20,
                         padding = 0),
                widget.TextBox(
                         text='\uE0B2',
                #                   #text='❰',
                #                   #text='◀',
                #                   text='🠴',
                         background = colours[1],
                         foreground = colours[4],
                #                   margin_y=19,
                                   padding=0,
                                   fontsize=17
                                   ),
 
                widget.Battery(format='{percent:2.0%} ', notify_below=0.3,
                        padding=0,
                background=colours[4]),
                #foreground = colours[1]),
                widget.TextBox("", name="default"),
                widget.Clock(format='%Y-%m-%d %a %H:%M:%S',
                         background = colours[3]),
            ],
            22,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
               #widget.CurrentLayout(),
                widget.GroupBox(font='scientifica',
                     highlight_method='text',
                    # margin_y =3,
                    # margin_x =2,
               # active = colours[3],
               # foreground = colours[1],
               # background = colours[1],
                margin_y =3,
                margin_x =2, 
                active=colours[0],
                inactive=colours[1],
                foreground=colours[3],
                                ),
                widget.WindowName(),
                # widget.CheckUpdates(
                #     colour_no_updates =colours[0],
                #     colour_have_updates = colours[3]
                #        ),
                widget.TextBox(
                    #    margin_y =3,
                    #    margin_x =2,
                    #text='❰',
                    #text='kurwa',
                    background = colours[1],
                    foreground = colours[3],
                    padding=0,
                    fontsize=10
                    ),
                widget.Battery(format='{percent:2.0%} ', notify_below=0.3,
                         #margin_y =28,
                    margin_y =3,
                    margin_x =2,
                    background = colours[3],
                    foreground = colours[1],
                     ),
                widget.TextBox("", name="default"),
                #widget.TextBox("", foreground="#d75f5f"),
                widget.Clock(format='%Y-%m-%d %a %H:%M:%S'),
            ],
            22,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#######################################################
############### assgin apps to groups ##################
########################################################
@hook.subscribe.client_new
def assign_app_group(client):
     d = {}
     #####################################################################################
     ### Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
     #####################################################################################
     
     d[group_names[0]] = ['brave-browser', 'Navigator']
     d[group_names[1]] = ['fluent-reader', 'org.pwmt.zathura']
     d[group_names[2]] = ['Alacritty'] 
     d[group_names[3]] = ['thunar'] 
     d[group_names[4]] = ['joplin'] 
     d[group_names[5]] = ['virt-manager', 'VirtualBox Manager']
     d[group_names[6]] = ['vscodium','rstudio', 'Fritzing','notepadqq-bin']
     d[group_names[7]] = ['caprine', 'signal']
     d[group_names[8]]=['superproductivity']
     d[group_names[9]] = ['com.rafaelmardojai.Blanket', 'crx_cinhimbnkkaeohfgghhklpknlkffjgod','crx_eikjhbkpemdappjfcmdeeeamdpkgabmk']
     # d[group_names[2]] = ['brave', 'librewolf']
     #d[group_names[2]] = ['alacritty'] 
     #d[group_names[2]] = [terminal] 
     wm_class = client.window.get_wm_class()[0]

     for i in range(len(d)):
         if wm_class in list(d.values())[i]:
             group = list(d.keys())[i]
             client.togroup(group)
             client.group.cmd_toscreen(toggle=False)

# ND
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
#wmname = "LG3D"
wmname = "qql"
