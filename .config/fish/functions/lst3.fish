function lst3
    if count $argv > /dev/null
        exa -Ta --level 4 .
    else
        exa -Ta --level 4 $argv
    end
end
