function vars
    set -U arguments --group-directories-first --icons --sort=accessed
    set -U EXA_ICON_SPACING 2
    set -U Fish_ItemCount (exa -l | wc -l)
    set -U Fish_ItemBreak 20
end