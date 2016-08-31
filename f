#!/usr/bin/env bash
if [[ $1 == "-i" || $1 == "interactive" ]]; then
  source f-s
fi
eval $(python f-i "$@")
