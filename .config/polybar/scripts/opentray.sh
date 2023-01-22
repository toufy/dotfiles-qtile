#!/bin/sh
trayactive=$(pgrep -f "polybar systray")
if [ -n "$trayactive" ]; then
    kill -TERM "$trayactive";
else
    polybar systray;
fi;
