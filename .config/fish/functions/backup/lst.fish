# Defined via `source`
function lst --wraps='exa -Ta --level 1' --description 'alias lst exa -Ta --level 1'
  exa -Ta --level 1 $argv; 
end
