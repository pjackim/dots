function lst
    if count $argv > /dev/null
        exa -Ta --level 1 .
    else
        exa -Ta --level 1 $argv
    end
end
