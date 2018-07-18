"""
链接一个数据库步骤：
    安装驱动  pip install redis
            pip install python-redis
    链接模块
    操作redis   key - values
"""
from time import sleep

import redis

# redis.Redis()
# 推荐使用下面这个方法 函数名和指令名基本一直
client = redis.StrictRedis()

client.set("name","Tom")

print(client.get("name").decode("utf8"))

# 设置过期时间
client.setex("action", 10 ,"sleeping")

print(client.get("action").decode("utf8"))

sleep(10)

print(client.get("action"))