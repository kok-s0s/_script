#!/bin/bash

echo "Welcome to Bash"
echo Welcome to Bash
echo 'text in quotes'
echo Hello world !
echo 'Hello world !'
echo "Hello world \! outdate" # 现在双引号支持包含一些特殊字符

# 分号在 Bash shell 中用作命令间的分隔符

echo ""
printf "Hello world !\n" # printf 命令用于格式化输出
printf "%-10s %-8s %-4s\n" No Name Mark # - 表示左对齐，10s 表示占 10 个字符宽度，8s 表示占 8 个字符宽度，4s 表示占 4 个字符宽度
printf "%-10s %-8s %-4.2f\n" 1 Sarath 80.3456
printf "%-10s %-8s %-4.2f\n" 2 James 90.9989
printf "%-10s %-8s %-4.2f\n" 3 Jeff 77.564

echo ""
echo "1\t2\t3"


