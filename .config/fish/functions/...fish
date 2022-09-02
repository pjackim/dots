function ..
    if count $argv > /dev/null
        cd ../$argv
    else
        cd ../ $argv
    end
end