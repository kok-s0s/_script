# env

所有的编程语言都利用变量来存放数据，以备随后使用或修改。

和编译型语言不同，大多数脚本语言不要在创建变量之前声明其类型。

用到什么类型就是什么类型。

在 shell 中，变量名前面加上个一个美元符号`$`，就可以访问变量的值。

```bash
nickname="kok-s0s"

echo $nickname
```

同时，在 shell 中定义了一些变量，用于保存用到的配置信息，比如可使用的打印机、搜索路径等，这些变量又叫做**环境变量**。

> 所有的应用程序和脚本都可以访问环境变量。可以使用`env` 或`printenv`命令查看当前 shell 中所定义的全部环境变量。

---

变量名由一系列字母、数字和下划线组成，其中不包含空白字符。

惯例：在脚本中使用大写字母命名环境变量，使用驼峰命名法或小写字母命名其它变量。

[env.sh](../script/env.sh)
