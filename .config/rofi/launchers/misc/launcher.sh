#!/usr/bin/env bash

## Author  : Aditya Shakya
## Mail    : adi1090x@gmail.com
## Github  : @adi1090x
## Twitter : @adi1090x

# Available Styles
# >> Created and tested on : rofi 1.6.0-1
#
# blurry	blurry_full		kde_simplemenu		kde_krunner		launchpad
# gnome_do	slingshot		appdrawer			appdrawer_alt	appfolder
# column	row				row_center			screen			row_dock		row_dropdown

theme="screen"
dir="$HOME/.config/rofi/launchers/misc"

# comment these lines to disable random style
themes=($(ls -p --hide="launcher.sh" $dir))
theme="blurry.rasi"

# rofi -show combi -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
# rofi -show ssh -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
# rofi -show run -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
# rofi -show window -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
# rofi -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
rofi -show-icons -no-lazy-grab -show drun -modi "ssh,drun,run" -theme $dir/"$theme" -show

