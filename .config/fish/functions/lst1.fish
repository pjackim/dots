function lst1
    if count $argv > /dev/null
        exa -Ta --level 2 .
    else
        exa -Ta --level 2 $argv
    end
end
