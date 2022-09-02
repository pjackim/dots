function home
    if count $argv > /dev/null
        cd $HOME/$argv
    else
        cd $HOME/ $argv
    end
end
