# File descriptors and Redirect

文件描述符是与输入和输出流相关联的整数。

系统预留 0、1 和 2。

| 文件描述符 |       含义        |
|:----------:|:---------------:|
|     0      | (标准输入) stdin  |
|     1      | (标准输出) stdout |
|     2      | (标准错误) stderr |

`>` 将左边的内容重定向至新的文本中，会清除原先文本中存在的内容。

`>>` 会将左边的内容追加在右边的文本中，不会清除原先文本中存在的内容。

`/dev/null` 是一个特殊的设备文件，它会丢弃接受到的任何数据。null 设备通常也被称为**黑洞**，凡是进入其中的数据都将一去不返。

## 自定义文件描述符

`exec` 命令创建全新的文件描述符。

[file_descriptors_and_redirects.sh](../script/file_descriptors_and_redirects.sh)

