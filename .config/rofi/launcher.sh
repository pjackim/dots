#!/usr/bin/env bash

# No args - run applicaiton selector
# $1
#       -c      = clipboard history
#       -run    = indicates to use rofi to open a directory and execute a file
#           $2  - Directory to open
#           $3  - Optional execution prefix

theme="blurry.rasi"
dir="$HOME/.config/rofi/launchers/misc"

if [ $# -eq 0 ]; then
    rofi -show-icons -no-lazy-grab -show drun -modi "ssh,drun,run" -theme $dir/"$theme"
elif [ "$1" = "-c" ]; then
    theme="blurry_noicon.rasi"
    rofi -modi " :greenclip print" -show " " -run-command '{cmd}' -theme $dir/"$theme"
elif [ "$1" = "run" ]; then

    files=$(find $2 -type f -name "*" | sed 's|.*/||')
    SCRIPT=$(rofi -dmenu -i -no-custom -p "Select Script" -show-icons -theme $dir/"$theme" -only-match -format s <<< $files)

    if [ $# -eq 3 ]; then
        eval "$3 $SCRIPT"
    else
        if [ -x "$SCRIPT" ]; then
            eval "./$SCRIPT"
        else
            file_ext="${SCRIPT##*.}"
            executor=""
            case $file_ext in
                py) executor="python3";;
                sh) executor="bash";;
                *) executor="";;
            esac
            eval "$executor $SCRIPT"
        fi
    fi 
fi
