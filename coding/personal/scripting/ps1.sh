# Define some basic colors using tput (8-bit color: 256 colors)
 bg="\[$(tput setaf 10)\]"
 usr="\[$(tput setaf 6)\]"
 host="\[$(tput setaf 2)\]"
 accent="\[$(tput setaf 1)\]"
 directory="\[$(tput setaf 1)\]"




bold="\[$(tput bold)\]"
reset="\[$(tput sgr0)\]"

# Define basic colors to be used in prompt
## The color for username
username_color="${reset}${bold}${usr}\$([[ \${EUID} == 0 ]] && echo \"${accent}\")";

## Color of @ and ✗ symbols (accent)
at_color=$reset$accent

## Color of host/pc-name
host_color=$reset$host

## Color of current working directory
directory_color=$reset$directory

## Color for other characters
etc_color=$reset$bg

# If last operation did not succeded, add [✗]- to the prompt
on_error="\$([[ \$? != 0 ]] && echo \"${etc_color}[${at_color}X${etc_color}]─\")"

# The last symbol in prompt ($, for root user: #)
symbol="${reset}${bold}${accent}$(if [[ ${EUID} == 0 ]]; then echo '#'; else echo ''; fi)"


# Setup the prompt/prefix for linux terminal
PS1="${etc_color}┌─┤${on_error}";
PS1+="${username_color}\u"; # \u=Username
PS1+="${at_color}@";
PS1+="${host_color}\h" #\h=Host
PS1+="${etc_color} [";
PS1+="${directory_color}\w"; # \w=Working directory
PS1+="${etc_color}]\n${etc_color}└──${at_color}╼ "; # \n=New Line
PS1+="${symbol}${reset}";

export PS1
