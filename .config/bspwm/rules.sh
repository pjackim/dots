#!/bin/sh
bspc config normal_border_color \#836A5000
bspc config focused_border_color \#D9A362
bspc config presel_feedback_color \#D9A36244

bspc config border_width         2
bspc config window_gap           5

bspc config split_ratio          0.52
bspc config borderless_monocle   true
bspc config gapless_monocle      true
bspc config single_monocle       true
bspc config center_pseudo_tiled  false

height_full=937 height_half=462 

left_x=5 right_x=1434
center_x=491
y_top=71 y_mid=543
width=477 center_width=938

# General Rules
    # Floating
    bspc rule -a konsole:term_f state=floating rectangle="400"x"500"+"760"+"340"
    bspc rule -a kitty:term_f state=floating rectangle="400"x"500"+"760"+"340"
    bspc rule -a deepin-calculator border=off state=floating layer=above rectangle="400"x"500"+"$left_x"+"$y_top"


    # Center
    bspc rule -a konsole:center state=floating rectangle="938"x"938"+"$y_top"+"$center_x"
    bspc rule -a *:center state=floating rectangle="938"x"938"+"$y_top"+"$center_x"


bspc rule -a *:Desktop-m1 desktop='^14' state=floating layer=below border=off rectangle="481"x"410"+"2515"+"595" 
bspc rule -a *:Desktop-m2-2 desktop='^24' state=floating layer=below border=off rectangle="481"x"410"+"3005"+"70" 
bspc rule -a *:Desktop-m2-1 desktop='^24' state=floating layer=below border=off rectangle="481"x"930"+"4435"+"70" 
bspc rule -a *:Desktop-m3-1 desktop='^1' state=floating layer=below border=off rectangle="950"x"410"+"71"+"50"
bspc rule -a Desktop:integrated_terminal_0 desktop='^14' state=floating rectangle="481"x"410"+"2515"+"595" layer=below border=off
bspc rule -a Desktop:integrated_terminal_1 desktop='^24' state=floating rectangle="950"x"410"+"71"+"50" layer=below border=off
bspc rule -a Desktop:integrated_terminal_1 desktop='^24' state=floating rectangle="950"x"410"+"71"+"50" layer=below border=off

# bspc rule -a lichess-nativefier-ab72a5 desktop='^10' state=floating layer=below border=off rectangle="461"x"400"+"2525"+"605" 

bspc rule -a lichess-nativefier-ab72a5 desktop='^24' state=floating layer=below border=off rectangle="461"x"400"+"3015"+"75"
bspc rule -a chess-nativefier-0b0e22 desktop='^24' state=floating layer=below border=off rectangle="461"x"930"+"3015"+"75"




bspc rule -a java-util-concurrent-ForkJoinWorkerThread state=floating
bspc rule -a feh state=floating
bspc rule -a tk state=floating
bspc rule -a Tk state=floating
bspc rule -a rdesktop state=floating
bspc rule -a thunar state=floating
bspc rule -a Opera::"Picture in Picture" state=floating

bspc rule -a yakuake state=floating rectangle="1920"x"864"+"0"+"160" border=off

bspc config external_rules_command "$(which external_rules)"
