#!/bin/bash

no1=4
no2=5

let result=no1+no2
echo $result

let no1++
echo "no1="$no1

let no1--
echo "no1="$no1

let no2+=6
echo "no2="$no2

let no2-=6
echo "no2="$no2

result=$[ no1 + no2]
echo $result

result=$[ $no1 + 13]
echo $result

result=$(( $no1 + $no2 + 1))
echo $result

result=$(expr $no1 + $no2 + 3)
echo $result

result=`expr $no1 + $no2 + 6`
echo $result

echo "4 * 0.56" | bc

no=54
result=`echo "$no * 1.5" | bc`
echo $result

echo "scale=2; 3/8" | bc

no=100
echo "obase=2; $no" | bc

no=1100100
echo "obase=10; ibase=2; $no" | bc

echo "sqrt(100)" | bc
echo "10^10" | bc
