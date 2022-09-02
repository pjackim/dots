#!/usr/bin/env bash

DIR="$HOME/.config/polybar/shapes"

# Launch the bar
polybar -q primary -c "$DIR"/config.ini &
polybar -q secondary -c "$DIR"/config.ini &
polybar -q tertiary -c "$DIR"/config.ini &
