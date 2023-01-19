# Repeat

有时候命令只有在满足某些条件时才能够被执行成功。

```bash
repeat()
{
  while true
  do
    $@ && return
  done
}
```

或

```bash
repeat() { while true; do $@ && return; done }
```

函数 repeat() 中包含了一个无限 while 循环，该循环执行以函数参数形式（通过 `$@` 访问）传入的命令。如果命令执行成功，则退出循环。

## 更快的做法

在大多数现代系统中，true 是作为 `/bin` 中的一个二进制文件来实现的。这就意味着每执行一次之前 repeat 函数里的 while 循环，shell 就不得不生成一个进程。为了避免这种情况，可以使用 shell 的内建命令 `:`，该命令的推出状态总为 0。

```bash
repeat() { while :; do $@ && return; done }
```

## 加入延时

假设需要使用 repeat 函数从 Internet 上下载一个暂时不可用的文件，不过这个文件只需要等一会就能下载。

每 30 秒执行一次 repeat 函数

```bash
repeat() { while :; do $@ && return; sleep 30; done }
```
