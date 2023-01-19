# Field Separator and Iterator

**内部字段分隔符（Internal Field Separator, IFS）

IFS 主要用于处理文本数据。

IFS 是一个环境变量，其中保存了用于分隔的字符，是当前 shell 环境使用的默认定界字符串。

eg： 处理 CSV 文件（逗号分割型数据 Comma Separated Value，CSV）

```bash
data="name,gender,rollno,location"

oldIFS=$IFS
IFS=,
for item in $data;
do
  echo Item: $item
done

IFS=$oldIFS
```

IFS 的默认值为空白字符（换行符、制表符或者空格）。

当 IFS 被设置为逗号时，shell 将逗号视为一个定界符。

eg：打印用户以及他们默认的 shell

```bash
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
```

## 循环

1. 面向列表的 for 循环

```bash
for var in list;
do
  commands; # 其中使用变量 $var
done
```

list 可以是一个字符串，也可以是一个值序列。

可以使用 echo 命令生成各种值序列：

```bash
echo {1..50}; # 生成一个从 1~~50的数字序列
echo {a..z} {A..Z}; # 生成大小写字母序列
```

```bash
for i in {a..z}; do actions; done
```

2. 迭代指定范围的数字

```bash
for((i=0;i<10;i++))
{
  commands; # 使用变量 $i
}
```

3. 循环到条件满足为止

```bash
while condition
do
  commands;
done
```

4. until 循环

```bash
x=0;
until [ $x -eq 9 ];
do
  let x++;
  echo $x;
done
```

[field_separator_and_iterator.sh](../script/field_separator_and_iterator.sh)
