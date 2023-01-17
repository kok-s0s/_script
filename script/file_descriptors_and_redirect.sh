#!/bin/bash

echo "This is a simple text 1" > temp.txt

echo "This is a simple text 2" >> temp.txt

cat temp.txt

cat temp.txt | tee temp2.txt | cat -n

echo this is a text line > input.txt
exec 3<input.txt
cat <&3
exec 4>input.txt
echo newline >&4
cat input.txt
exec 5>>input.txt
echo appended line >&5
cat input.txt
