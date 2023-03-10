**简单命令的组合是一门艺术，实践得越多，收益就越大。**

# \_script

> shebang 这个词其实是两个字符名称（sharp-bang）的简写。在 Unix 的行话里，用 sharp 或 bash（有时候是 mesh）来称呼字符#，用 bang 来称呼字符!。所以 shebang 就是指#!，即“井号感叹号”（#!）。这个字符组合在 Unix 的脚本中有着特殊的意义，它是一个“魔法”字符组合，用来告诉系统这个脚本需要什么解释器来执行。

shell 脚本通常以 shebang 起始，即 `#!`，后跟解释器的路径，如：

```bash
#!/bin/bash
```

脚本的执行方式：

1. 将脚本名作为命令行参数：

```bash
bash myScript.sh
```

> 如果将脚本作为 bash 的命令行参数来运行，那么就用不着使用 shebang 了。可以利用 shebang 来实现脚本的独立运行。可执行脚本使用 shebang 之后的解释器路径来解释脚本。

2. （**个人优先使用**）授予脚本执行权限，将其变为可执行文件：

```bash
chmod 755 myScript.sh
./myScript.sh
```

或（注意以下的授权能让所有用户都可以执行该脚本）

```bash
chmod a+x myScript.sh
./myScript.sh
```

## 多敲就对了

> 可以使用 [delete_everything.sh](/script/delete_everything.sh) 脚本来删除因执行测试脚本而产生的文件。

[echo.sh](./script/echo.sh)

[env](./chapter/env.md)

[shell_built-in_features](./chapter/shell_built-in_features.md)

[math_calculation](./chapter/math_calculation.md)

[File descriptors and Redirect](./chapter/file_descriptors_and_redirect.md)

[Array and Associative array](./script/array_and_associative_array.sh)

[alias](./script/alias.sh)

[get Terminal Info](./script/get_terminal_info.sh)

[date](./chapter/date.md)

[function and param](./script/func_param.sh)

[Combine commands](./chapter/combine_commands.md)

[read.sh](./script/read.sh)

[repeat](./chapter/repeat.md)

[Field Separator and Iterator](./chapter/field_separator_and_iterator.md)

[Compare and Test](./chapter/compare_and_test.md)

[cat](./chapter/cat.md)

[scriptplay](./chapter/scriptplay.md)

## ta 人的文章

- [初学者应该知道的 Linux 网络命令](https://www.freecodecamp.org/chinese/news/linux-networking-commands-for-beginners/) --- [实践](./script/web.sh)

- [How to Debug a Shell Script](https://stackpointer.io/unix/how-to-debug-shell-script/345/#:~:text=How%20to%20Debug%20a%20Shell%20Script%201%20Shell,3%20Custom%20Function%20to%20Debug%20Shell%20Script%20)
