#!/bin/bash

# remove unwanted VSCode extension(s)
sudo code --uninstall-extension eamodio.gitlens

# change default git config to ignore chmod changes and symbolic links
git config core.fileMode false

# change pull to alway rebase to eliminate common git error
git config pull.rebase true

# set up first-run-notice
cp .devcontainer/first-run-notice.txt /workspaces/.codespaces/shared/first-run-notice.txt

# cp .devcontainer/.dircolors /home/$GITHUB_USER
cp .devcontainer/.dircolors ~
cp .devcontainer/.bash_aliases ~

# just for the scavenger hunt
python .devcontainer/subfolder.py
