function update
  sudo pacman -Syyu $argv; 
end

function sync
  sudo pacman -Syy $argv; 
end

function uninstall_ful
  sudo pacman -Rncs $argv; 
end

function uninstall
  sudo pacman -R $argv; 
end

function install
  sudo pacman -S $argv; 
end

