# Defined via `source`
function lst4 --wraps='exa -Ta --level = 5' --description 'alias lst4 exa -Ta --level = 5'
  exa -Ta --level 5 $argv; 
end
