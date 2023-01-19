#!/bin/bash

# 在不按下回车键的情况下读入 n 个字符

# 从输入中读入 n 个字符并存入变量 variable_name
# read -n number_of_chars variable_name
read -n 7 var
echo $var

# 用无回显的方式读取密码
read -s var
echo $var

# 使用 read 显示提示信息
read -p "Enter input:" var
echo $var

# 在给定时限内读取输入
# read -t timeout var
read -t 2 var # 两秒内的输入
echo $var

# 用特定的定界符作为输入行的结束
# read -d delim_char var
read -d ":" var
echo $var
