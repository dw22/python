# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
# host = socket.gethostname()
host = '192.168.1.116'
# 设置端口好
port = 9999

# 连接服务，指定主机和端口
sk.connect((host, port))

# 接收小于 1024 字节的数据
msg = sk.recv(1024)

sk.close()

print (msg.decode('utf-8'))
print (host)