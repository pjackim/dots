#!/usr/bin/env bash

# $1 = directory for scripts
#export PYTHONPATH=’/home/pjackim/.pyenv/customlibs/’
getExecutor() {
    if echo "$1" | grep -q '\.'; then
        file_ext="${1##*.}"
        exe_type=""
        case $file_ext in
            py) exe_type="python3";;
            sh) exe_type="bash";;
            java) exe_type="java";;
            *) exe_type="";;
        esac
        echo "$exe_type"
    else
        echo ""
    fi
}

SCRIPT=$(find $1 -maxdepth 1 -type f | sed 's|.*/||' | rofi -sort -dmenu -i -show-icons -p "$2: " -theme blurry_noicon )

if [ -n "$SCRIPT" ]; then
    EXE=$(getExecutor $SCRIPT)
    eval "$EXE $1$SCRIPT"
fi
