#!/usr/bin/env bash
args="$@"
if [[ $1 == "-i" || $1 == "interactive" ]]; then
  source f-s
else
    eval $(./f-i $args)
    if [ ! $? -eq 0 ]; then
	thefuck $F
    fi
fi
