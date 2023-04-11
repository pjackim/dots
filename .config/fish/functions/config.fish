function config
    if count $argv > /dev/null
        cd $HOME/.config/$argv
    else
        cd $HOME/.config/ $argv
    end
end
