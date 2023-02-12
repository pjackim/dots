set -x PATH $PATH /sbin/

set -gx SCRIPTING /home/pjackim/coding/personal/scripting/
set -gx CS314 /home/pjackim/coding/school/junior/cs314/
set -gx PERSONAL /home/pjackim/coding/personal/scripting/

set PYENV_ROOT $HOME/.pyenv
set -x PATH $PYENV_ROOT/shims $PYENV_ROOT/bin $PATH
pyenv rehash


function autostart_fish
    ~/bin/autostart/startup
end


function split
    kitty ./ &
end


