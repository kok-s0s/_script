# scriptplay

录制并回放终端会话

```bash
# 开始录制终端会话
script -t 2> timing.lg -a output.session

# 演示
ls
ll
cls

# 推出录制
exit

# 回放命令执行过程
scriptreplay timing.log output.session
```
