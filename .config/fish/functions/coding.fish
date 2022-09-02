function coding
    if count $argv > /dev/null
        cd $HOME/coding/$argv
    else
        cd $HOME/coding/ $argv
    end
end
