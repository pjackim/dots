#!/usr/bin/env bash

# No args - run applicaiton selector
# $1
#       -c      = clipboard history


theme="blurry.rasi"
dir="$HOME/.config/rofi/launchers/misc"

style() {
    file_ext="${$1##*.}"
    style_type=""
    case $file_ext in
        py) executor="python3";;
        sh) executor="bash";;
        *) executor="";;
    esac
    echo -en "$1\0icon\x1f$style_type\n"
}

if [ $# -eq 0 ]; then
    rofi -show-icons -no-lazy-grab -show drun -modi "ssh,drun,run"
elif [ "$1" = "-c" ]; then
    rofi -modi " :greenclip print" -show " " -run-command '{cmd}' -theme blurry_noicon
fi
