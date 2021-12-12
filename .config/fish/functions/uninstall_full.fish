# Defined via `source`
function uninstall_full --wraps='sudo pacman -Rncs' --description 'alias uninstall_full sudo pacman -Rncs'
  sudo pacman -Rncs $argv; 
end
