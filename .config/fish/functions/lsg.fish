# Defined via `source`
function lsg --wraps=ls --description 'includes github'
    #echo "- : not modified"
  command exa --icons --long --git --no-permissions --header --no-time --changed --no-user --no-filesize --sort=type $argv; 
end
