#!/bin/sh
killall -s SIGUSR1 qtile
"$XDG_CONFIG_HOME"/qtile/scripts/startup.sh
