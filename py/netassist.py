# Created by: kok-s0s
# Last Modified at: Wed Mar 12 16:44:50 2025
# File Name: netassist.py

import socket

# 目标服务器地址和端口
host = "192.168.21.10"
port = 6666

# 创建 TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.settimeout(
    5
)  # 设置超时时间 5 秒, 防止 recv() 阻塞，超过 5 秒都没有传完给我反思下是弄了啥子哦
print(f"Connected to {host}:{port}")

# 发送数据
data_to_send = '{"g":{"pallet.data":null}}\r'  # 可变，根据实际情况修改

sock.sendall(data_to_send.encode("utf-8"))

# 接收数据（不限制长度，读取完整响应）
response_data = b""
try:
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response_data += chunk
except socket.timeout:
    print("Timeout reached, stopping receive.")

# 打印完整数据
print(f"Received: {response_data.decode('utf-8', errors='ignore')}")

# 关闭连接
sock.close()
