# shell built-in features

1. 获取字符串的长度

可以用以下的写法来获得变量值的长度：

```bash
length=${#var}
```

eg:

```bash
var=12345678901234567890
echo ${#var}
```

`length` 即字符串中所包含的字符数。

2. 识别当前所使用的 shell

可以通过环境变量 `SHELL` 知道当前使用的是哪个 shell：

```bash
echo $SHELL
```

3. 检查是否为超级用户

```bash
if [ $UID -eq 0 ]; then
    echo "You are root."
else
    echo "You are just an ordinary user."
fi
```

环境变量 `UID` 中保存的是用户 `ID`。

root 用户的 `UID` 是 0。

上面这个代码片段可以用于检查当前脚本是以 root 用户还是以普通用户的身份运行的。

[shell_built-in_features.sh](../script/shell_built-in_features.sh)
