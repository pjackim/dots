function school
    if count $argv > /dev/null
        cd $HOME/coding/school$argv
    else
        cd $HOME/coding/school $argv
    end
end
