
function initVars
    set -g arguments --group-directories-first --icons --sort=accessed
    set -gx EXA_ICON_SPACING 2
    set -g Fish_ItemCount (exa -l | wc -l)
    set -g Fish_ItemBreak 20
end

function ls
    initVars

    if test $Fish_ItemCount -lt $Fish_ItemBreak
        command exa -1 $arguments $argv;
    else
        command exa -G $arguments $argv;
    end
end

function la
    initVars
    command exa -aG $arguments $argv;
end

function ll
    initVars
    exa -al1 $arguments $argv; 
end

function lst
    if any-arguments $argv
        command exa -Ta --level $argv; 
    else
        command exa -Ta --level 1;
    end
end

