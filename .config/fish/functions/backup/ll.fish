# Defined via `source`
function ll --wraps='exa -al ' --description 'alias ll exa -al '
  exa -al  $argv; 
end
