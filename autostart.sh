#!/bin/bash

#xrandr --output VGA-1 --mode 1366x768 --scale 1.27x1.27 --panning 1734x975
xrandr --output VGA-1 --mode 1366x768 --scale 1.40x1.40 --panning 1912x1075
feh --bg-fill /home/em0n/Pictures/wallpapers/black-illusion.jpg
#feh --bg-fill /home/em0n/Pictures/wallpapers/black-illusion.jpg
#feh --bg-fill /home/em0n/Pictures/wallpapers/windows-10.jpg

picom &
greenclip daemon &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#xrandr --output VGA-1 --mode 1366x768 --scale 1x1 --panning 1366x768
#xrandr --output VGA-1 --mode 1366x768 --scale 1.25x1.25 --panning 1708x960
#xrandr --output VGA-1 --mode 1366x768 --scale 1.3x1.3 --panning 1776x998
#xrandr --output VGA-1 --mode 1366x768 --scale 1.406x1.406 --panning 1920x1080
#xrandr --output VGA-1 --mode 1366x768 --scale 1.28x1.28 --panning 1748x983
#xrandr --output VGA-1 --mode 1366x768 --scale 1.27x1.27 --panning 1734x975

