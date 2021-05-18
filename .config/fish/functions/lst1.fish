# Defined via `source`
function lst1 --wraps='exa -Ta --level = 2' --description 'alias lst1 exa -Ta --level = 2'
  exa -Ta --level = 2 $argv; 
end
