#!/bin/sh

DEFAULT='#282a36'
ALT='#44475a'
PRIMARY='#d6acff'
SECONDARY='#ff92df'
INPUT='#8be9fd'
DELETE='#ffffa5'
VERIFY='#69ff94'
WRONG='#ff6e6e'

i3lock \
--insidever-color=$ALT      \
--ringver-color=$VERIFY     \
--insidewrong-color=$ALT    \
--ringwrong-color=$WRONG    \
--inside-color=$DEFAULT     \
--ring-color=$PRIMARY       \
--line-color=$SECONDARY     \
--separator-color=$ALT      \
--verif-color=$VERIFY       \
--wrong-color=$WRONG        \
--time-color=$SECONDARY     \
--date-color=$SECONDARY     \
--keyhl-color=$INPUT        \
--bshl-color=$DELETE        \
--blur 10                   \
--clock                     \
--time-str="%H:%M:%S"       \
--date-str="%A, %d/%m/%Y"   \
