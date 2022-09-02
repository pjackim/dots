function ls

    if test $Fish_ItemCount -lt $Fish_ItemBreak
        command exa -1 $arguments $argv;
    else
        command exa -G $arguments $argv;
    end
end