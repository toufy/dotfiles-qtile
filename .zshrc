#env
export ZSH="$HOME/.oh-my-zsh"
ZSH_CONF="$HOME/.zsh"
SCRIPTS_DIR="$HOME/scripts"
fpath+=${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions/src

#settings
ZSH_THEME="darkblood"
CASE_SENSITIVE="true"
COMPLETION_WAITING_DOTS="true"

#plugins
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

#src
source $ZSH/oh-my-zsh.sh
source $ZSH_CONF/.aliases
source $ZSH_CONF/.dracula.zsh

#on_start
$SCRIPTS_DIR/color-scripts/./randomcolor.py
