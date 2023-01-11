# mathematical calculation

Bash shell 使用 `let`、`(())` 和 `[]` 执行基本的算术操作。

`let` 命令可以执行基本的算术操作，当使用 `let` 时，变量名之前不再需要添加 `$`。

工具 `expr` 和 `bc` 可以用来执行高级操作。

`bc` 是一个用于数学运算的高级实用工具，这个精密的计算器包含了大量的选项。可以借助它执行浮点数运算并使用一些高级函数

```bash
echo "4 * 0.56" | bc

no=54
result=`echo "$no * 1.5" | bc`
echo $result
```

`bc` 可以接受操作控制前缀，这些前缀之间使用分号分割。

- 设定小数精度

```bash
echo "scale=2; 3/8" | bc
```

- 进制转换

eg: 二进制和十进制的转换

```bash
no=100
echo "obase=2; $no" | bc

no=1100100
echo "obase=10; ibase=2; $no" | bc
```

- 计算平方及平方根

```bash
echo "sqrt(100)" | bc
echo "10^10" | bc
```

[math_calculation](../script/math_calculation.sh)
