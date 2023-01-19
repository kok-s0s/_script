# Compare and Test

## if 条件

```bash
if condition;
then
  commands;
fi
```

## else if 和 else

```bash
if condition;
then
  commands;
else if condition; then
  commands;
else
  commands;
fi
```

if 和 else 语句能够嵌套使用。

可使用逻辑运算符将条件判断部分简写

```bash
[ condition ] && action; # 如果 condition 为真，则执行 action。
[ condition ] || action; # 如果 condition 为假，则执行 action。
```

## 算术比较

比较条件通常被放置在封闭的中括号内。

一定要注意在 `[` 和 `]` 与操作数之间有一个空格，如果忘记这个空格，脚本就会报错。

```bash
[ $var -eq 0 ] # 当$var等于0时，返回真
[ $var -ne 0 ] # 当$var不为0时，返回真
```

- `-gt` - 大于
- `-lt` - 小于
- `-ge` - 大于或等于
- `-le` - 小于或等于
- `-a` - 逻辑与操作
- `-o` - 逻辑或操作

```bash
[ $var1 -ne 0 -a $var2 -gt 2 ]
[ $var1 -ne 0 -o $var2 -gt 2 ]
```

## 文件系统相关测试

- `[ -f $file_var ]` - 给定的变量包含正常的文件路径或文件名 - 返回真
- `[ -x $var ]` - 给定的变量包含的文件可执行 - 返回真
- `[ -d $var ]` - 给定的变量包含的是目录 - 返回真
- `[ -e $var ]` - 给定的变量包含的文件存在 - 返回真
- `[ -c $var ]` - 给定的变量包含的是一个字符设备文件的路径 - 返回真
- `[ -b $var ]` - 给定的变量包含的是一个块设备文件的路径 - 返回真
- `[ -w $var ]` - 给定的变量包含的文件可写 - 返回真
- `[ -r $var ]` - 给定的变量包含的文件可读 - 返回真
- `[ -L $var ]` - 给定的变量包含的是一个符号链接 - 返回真

## 字符串比较

用双中括号

1. 测试两个字符串是否相同

```bash
[[ $str1 = $str2]]
[[ $str1 == $str2]]
```

2. 测试两个字符串是否不同

```bash
[[ $str1 != $str2]]
```

3. 找出字母表中靠后的字符串

字符串是依据字符的 ASCII 值进行比较的。

```bash
[[ $str1 > $str2]]
[[ $str1 < $str2]]
```

4. 测试空串

```bash
[[ -z $str1 ]] # 如果str1为空串，则返回真
[[ -n $str1 ]] # 如果str1不为空串，则返回真
```

## test 命令

用来测试条件，避免使用过多的括号，增强代码的可读性。

```bash
if [ $var -eq 0 ]; then echo "True"; fi
```

等价于

```bash
if test $var -eq 0 ; then echo "True"; fi
```

注意，test 是一个外部程序，需要衍生出对应的进程。而 `[` 是 Bash 的一个内部函数，因此后者的执行效率更高。test 兼容于 Bourne shell、ash、dash等。

[compare_and_test.sh](../script/compare_and_test.sh)
