#!/usr/bin/env bash
args="$@"
eval $(f-i $args)
if [ $? -ne 0 ]; then
    thefuck $F
fi
