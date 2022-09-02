function lst2
    if count $argv > /dev/null
        exa -Ta --level 3 .
    else
        exa -Ta --level 3 $argv
    end
end
