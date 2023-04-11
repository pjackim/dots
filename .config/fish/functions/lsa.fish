# Defined via `source`
function lsa --wraps=ls --description 'sorts by name'
  command exa -aFG --sort=name; 
end
