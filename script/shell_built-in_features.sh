#!/bin/bash

var=12345678901234567890
echo ${#var}

echo $SHELL

if [ $UID -eq 0 ]; then
    echo "You are root."
else
    echo "You are just an ordinary user."
fi
