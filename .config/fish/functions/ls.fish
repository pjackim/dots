# Defined via `source`
function ls --wraps='exa -1 ' --description 'alias ls exa -1 '
  exa -1  $argv; 
end
