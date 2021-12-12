# Defined via `source`
function sync --wraps='sudo pacman -Syy' --description 'alias sync sudo pacman -Syy'
  sudo pacman -Syy $argv; 
end
