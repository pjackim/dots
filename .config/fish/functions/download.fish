function download
    if count $argv > /dev/null
        cd $HOME/downloads/$argv
    else
        cd $HOME/downloads/ $argv
    end
end
