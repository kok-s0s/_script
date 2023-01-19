#!/bin/bash

ls | cat -n > out.txt

# cmd_output=$(COMMANDS) 将命令序列的输出赋值给变量，也称为 `子shell` 法

cmd_output=$(ls | cat -n)
echo $cmd_output

pwd

(cd ~; ls)

pwd
