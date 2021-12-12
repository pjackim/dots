# Defined via `source`
function update --wraps='sudo pacman -Syyu' --description 'alias update sudo pacman -Syyu'
  sudo pacman -Syyu $argv; 
end
