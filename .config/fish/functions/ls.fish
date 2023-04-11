function ls
    if test $Fish_ItemCount -lt $Fish_ItemBreak
        command exa -F1 $arguments $argv;
    else
        command exa -FG $arguments $argv;
    end
end