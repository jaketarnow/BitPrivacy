#!/usr/bin/env bash
if [ "$(uname)" == "Darwin" ]; then
    $(brew install tor)
    $(brew install privoxy)
    $(sudo pip install selenium)
    # MAC OSX Platform
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Linux
    $(apt-get update)
    $(apt-get install tor)
    $(apt-get install privoxy)
    $(sudo pip install selenium)
fi