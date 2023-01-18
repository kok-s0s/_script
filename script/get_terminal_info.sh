#!/bin/bash

# tput

# stty

# 获取终端的行数和列数
tput cols
tput lines

# 打印出当前的终端名
tput longname
echo ""

# 将光标移动到坐标(100, 100)处
# tput cup 100 100

# 输入密码，禁止显示
echo -e "Enter password: "
# 在读取密码前禁止回显
stty -echo
read password
# 重新允许回显
stty echo
echo
echo Password read.
