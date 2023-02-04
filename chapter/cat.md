# cat

cat 表示 conCATenate（拼接）

cat 命令可以

1. 读取文件

2. 拼接数据

3. 能从标准输入中读取数据（利用管道操作符）

```bash
OUTPUT_FROM_SOME COMMANDS | cat
```

---

```bash
cat -s file # 去掉多余的空白行

cat -T file # 将制表符显示为^I

cat -n file # 显示行号
```

[cat.sh](../script/cat.sh)
