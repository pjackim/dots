# ~/.bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# -------------------------------------------
# 			Console Tag
# -------------------------------------------
if [ -f $HOME/coding/personal/scripting/ps1.sh ];
then
	. $HOME/coding/personal/scripting/ps1.sh
else
	PS1='\u@\h \W > '
fi

# pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"



# Ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

# -------------------------------------------
# 			Install Configs
# -------------------------------------------
alias install='sudo pacman -S'
alias uninstall='sudo pacman -R'
alias uninstall_full='sudo pacman -Rncs'
alias update='sudo pacman -Syyu'
alias sync='sudo pacman -Syy'

# -------------------------------------------
# 			Directory Configs
# -------------------------------------------
group_dirs='--group-directories-first --icons'

alias ls='exa -1 $group_dirs'
alias la='exa -a $group_dirs'
alias ll='exa -al $group_dirs'
alias lsa='la'

alias lst='exa -Ta --level=1'
alias lst1='exa -Ta --level=2'
alias lst2='exa -Ta --level=3'
alias lst3='exa -Ta --level=4'
alias lst4='exa -Ta --level=5'
alias lst5='exa -Ta --level=6'

alias ..='cd ..'
alias ...='cd ../..'
alias ..3='cd ../../..'

# -------------------------------------------
# 			Editors
# -------------------------------------------
alias vi='nvim'
alias vim='nvim'
alias py='python3'

# -------------------------------------------
# 			Shortcuts
# -------------------------------------------
alias home='cd "$HOME"'
alias config='cd "$HOME"/.config'

alias downloads='cd "$HOME"/downloads'
alias coding='cd "$HOME"/coding'
alias personal='cd "$HOME"/coding/personal'
alias scripting='cd "$HOME"/coding/personal/scripting'
alias school='cd "$HOME"/coding/school'

# Directories
alias d-polybar='config && cd polybar/shapes'
alias d-bspwm='config && cd bspwm'


alias sxhkd.mode='/home/pjackim/.config/sxhkd/scripts/sxhkd.mode'
if [ -d /home/pjackim/.local/bin ] ; then
 for f in /home/pjackim/.local/bin/* ; do
	 if [ -f "$f" ] ; then
		 alias $(basename "$f")='"$f"'
	fi
 done
 unset f
fi


# -------------------------------------------
# 			Applications
# -------------------------------------------

# -------------------------------------------
# 			PATH
# -------------------------------------------
# export PATH="$HOME/.local/bin:$PATH"
export PAGER="/bin/most"


# -------------------------------------------
# 			Typos
# -------------------------------------------
alias dwnld='downloads'
alias hoem='home'
alias clera='clear'
alias celar='clear'
. "$HOME/.cargo/env"


# -------------------------------------------
# 			Fish
# -------------------------------------------
exec fish

xset s off -dpms
# BEGIN_KITTY_SHELL_INTEGRATION
if test -n "$KITTY_INSTALLATION_DIR" -a -e "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; then source "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; fi
# END_KITTY_SHELL_INTEGRATION
