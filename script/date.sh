#!/bin/bash

# 在系统内部，日期被存储成一个整数，其取值为自1970年1月1日0时0分0秒起所流逝的秒数。这种计时方式称为纪元时或Unix时间

date

date +%s

date --date "Wed mar 15 08:09:16 EDT 2017" +%s

date --date "Jan 20 2001" +%A

date "+%d %B %Y"


# 计算一组命令所花费的执行时间

start=$(date +%s)
tree ~;
ls -a;
end=$(date +%s)
difference=$((end - start))
echo Time taken to execute commands is $difference seconds.

# date 命令的最小精度是秒。对命令计时的另一种更好的方式是使用 time 命令
# time commandOrScriptName


# 在脚本中生成延时
echo Count:
tput sc
# 循环 40 秒
for count in `seq 0 40`
do
  tput rc
  tput ed
  echo -n $count
  sleep 1
done
