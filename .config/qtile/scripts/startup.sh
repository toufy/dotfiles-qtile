#!/bin/sh
xset s off
xset s noblank
xset -dpms
setxkbmap -layout us,ar
setxkbmap -option 'grp:alt_shift_toggle'
feh --bg-fill "$BG_IMG"
for proc in dunst picom polybar udiskie 
    do
        procid=$(pgrep -f "$proc")
        if [ -n "$procid" ];then
            kill -KILL "$procid"
        fi;
done
udiskie -a &
picom &
polybar top &
dunst &
