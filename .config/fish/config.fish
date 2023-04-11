set -x PATH $PATH /sbin/

set -gx SCRIPTING /home/pjackim/coding/personal/scripting/
set -gx CONFIG /home/pjackim/.config/
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


