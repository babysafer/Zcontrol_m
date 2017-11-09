# encoding: utf-8
import os

DEBUG = True

#session 使用的secret key
SECRET_KEY = os.urandom(24)

# 到节点探测端口的socket超时时间
socket_time_out = 2

# 登录用户名密码,01,Paas@2017,02,Paas@2018
user_info = {
    'paas01': 'pbkdf2:sha256:50000$UWhZQLmY$a5d82d19c3a3069e300a3fbdd75ef0eba87f54e44a7d76b179eef258e216d049',
    'paas03':'pbkdf2:sha256:50000$F4R4psl2$f64242d5a9d20909b2c46a1a89be5f7c696ef3e21ed81c832bf92a59e65103d5',
    'paas02': 'pbkdf2:sha256:50000$FFGUSrnd$08a79f44fdc10b53d203512bddcd0ae8e4d2d14e45ea5e2e4fc10173f0817077'
}

# 目标zookeeper地址,ip的顺序请按myid的自然顺序排列 方便前台展示对应顺序
conn_str = {
    u'北京测试': '172.21.11.63:8501,172.21.11.64:8501,172.21.11.65:8501',
    u'北京hadoop': '172.21.11.66:11001,172.21.11.67:11001,172.21.11.73:11001',
    u'北京测试3': '172.21.11.63:8501,172.21.11.64:8501,172.21.11.65:8501',
    u'北京测试4': '172.21.11.63:8541,172.21.11.64:8541,172.21.11.65:8541',
    u'北京测试5': '172.21.11.63:8501,172.21.11.64:8501,172.21.11.65:8501',
    u'北京测试6': '172.21.11.63:8541,172.21.11.64:8541,172.21.11.65:8541',
    u'北京测试7': '172.21.11.63:8001,172.21.11.64:8001,172.21.11.65:8001'
}

# todo 如何在程序在程序中改变conn_str字典并写入文本文件
