# Defined via `source`
function install --wraps='sudo pacman -S' --description 'alias install sudo pacman -S'
  sudo pacman -S $argv; 
end
