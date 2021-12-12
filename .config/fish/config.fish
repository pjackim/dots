set -x PATH $PATH /sbin/

set -gx SCRIPTING /home/pjackim/coding/personal/scripting/
set -gx CS314 /home/pjackim/coding/school/junior/cs314/
set -gx PERSONAL /home/pjackim/coding/personal/scripting/




function autostart_fish
    ~/bin/autostart/startup
end


function split
    kitty ./ &
end


