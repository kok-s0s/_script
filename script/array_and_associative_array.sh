#!/bin/bash

array_var[0]="test1"
array_var[1]="test2"
array_var[2]="test3"
array_var[3]="test4"
array_var[4]="test5"
array_var[5]="test6"

echo ${array_var[0]}

index=5
echo ${array_var[$index]}

echo ${array_var[*]}
echo ${array_var[@]}

echo ${#array_var[*]}


declare -A ass_array

ass_array=([index1]=val1 [index2]=val2)
echo ${ass_array[index1]}
echo ${ass_array[index2]}

ass_array[index1]=val1
ass_array[index2]=val2
echo ${ass_array[index1]}
echo ${ass_array[index2]}

declare -A fruits_value
fruits_value=([apple]='100 dollars' [orange]='150 dollars')

echo "Apple costs ${fruits_value[apple]}"

echo ${!array_var[*]}
echo ${!ass_array[@]}
echo ${!fruits_value[*]}
