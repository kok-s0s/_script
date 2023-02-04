#!/bin/bash

echo "hello world" > cat_test.txt

cp cat_test.txt cat_test_02.txt

cat cat_test.txt cat_test_02.txt

cat cat_test.txt cat_test_02.txt > cat_test_03.txt

echo ""

cat cat_test_03.txt

echo ""

echo "kok-s0s" | cat - cat_test.txt
