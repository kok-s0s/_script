#!/bin/bash

data="name,gender,rollno,location"

oldIFS=$IFS
IFS=,
for item in $data;
do
  echo Item: $item
done

IFS=$oldIFS



line="root:x:0:0:root:/root:/bin/bash"
oldIFS=$IFS;
IFS=":"
count=0
for item in $line;
do
  [ $count -eq 0 ] && user=$item;
  [ $count -eq 6 ] && shell=$item;
  let count++
done;
IFS=$oldIFS
echo "$user's shell is $shell";


echo {1..50}; # 生成一个从 1~~50的数字序列
echo {a..z} {A..Z}; # 生成大小写字母序列


for((i=0;i<10;i++))
{
  echo i = $i; # 使用变量 $i
}


a=0
while [ $a -lt 10 ]
do
   echo a = $a
   let a++;
done


x=0;
until [ $x -eq 9 ];
do
  let x++;
  echo $x;
done
