# Defined via `source`
function lst3 --wraps='exa -Ta --level = 4' --description 'alias lst3 exa -Ta --level = 4'
  exa -Ta --level 4 $argv; 
end
