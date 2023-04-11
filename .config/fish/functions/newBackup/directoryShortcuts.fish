function coding
  cd /home/pjackim/coding/ $argv
end

function personal
  cd /home/pjackim/coding/personal/ $argv
end

function scripting
  cd /home/pjackim/coding/personal/scripting/ $argv 
end

function school
  cd /home/pjackim/coding/school/ $argv 
end

function home
  cd /home/pjackim/ $argv 
end

function hoem
  home $argv 
end

function config
  cd /home/pjackim/.config/ $argv 
end

function d-bspwm
  config && cd bspwm $argv 
end

function d-junior
    school && cd junior
    ls
end

function d-polybar
  config && cd polybar/shapes/ $argv 
end

function downloads
  cd /home/pjackim/downloads/ $argv 
end

function cdl
    cd $argv
    ls
end

function ...
  cd ../../ $argv 
end

function ..
  cd ../ $argv 
end

function ..3
  cd ../../../ $argv 
end
