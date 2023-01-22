#!/bin/sh
if [ $# -eq 1 ]
	then
		ans=$1
	else
		ans=$(zenity --warning \
		--title="session options" --text "what do you want to do?" \
		--ok-label="cancel" \
		--extra-button "suspend" \
		--extra-button "log-out" \
		--extra-button "restart" \
		--extra-button "shut down"
		)
fi
case $ans in
	"suspend")
		sh "$XDG_CONFIG_HOME/qtile/scripts/lock.sh"\
		&& systemctl suspend -i ;;
	"log-out")
		qtile cmd-obj -o cmd -f shutdown;;
	"restart")
		reboot;;
	"shut down")
		shutdown now;;
esac
