# Defined via `source`
function uninstall --wraps='sudo pacman -R' --description 'alias uninstall sudo pacman -R'
  sudo pacman -R $argv; 
end
