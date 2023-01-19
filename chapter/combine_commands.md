# Combine commands

Unix Shell 脚本最棒的特性之一就是可以轻松地将多个命令组合起来生成输出。

一个命令的输出可以作为另一个命令的输入，而这个命令的输出又会传递至下一个命令，以此类推。这种命令组合的输出可以被存储在变量中。

命令输入通常来自于 stdin 或参数。

输出可以发送给 stdout 或 stderr。

当组合多个命令时，通常将 stdin 用于输入，stdout 用于输出。

组合命令时，被组合的这些命令也被称为**过滤器（filter）**。

使用管道（pipe）连接每个过滤器，管道操作符为 `|`。

```bash
$ cmd1 | cmd2 | cmd3
```

```bash
ls | cat -n > out.txt

# cmd_output=$(COMMANDS) 将命令序列的输出赋值给变量，也称为 `子shell` 法

cmd_output=$(ls | cat -n)
echo $cmd_output
```

## 利用 `子shell` 生成一个独立的进程

`子shell` 本身就是独立的进程，可以使用 `()` 操作符来定义一个 `子shell`。

eg

```bash
$ pwd
$ (cd /bin; ls)
build  Desktop  Documents  Downloads  go  Music  Pictures  Public  Qt6  snap  Templates  Videos
$ pwd
```

当命令在 `子shell` 中执行时，不会对当前 shell 造成任何影响；所有的改变仅限于该 `子shell` 内。上面这个例子在用 cd 命令改变 `子shell` 的当前目录时，这种变化不会反映到 `主shell` 环境中。

[combine_commands.sh](../script/combine_commands.sh)
