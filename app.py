import os


# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 基础URL地址
BASE_URL = "http://ihrm-test.itheima.net"

# 存放token
TOKEN = None

# 存放请求头数据
headers_data = {
    "Content-Type":"application/json",
    "Authorization":"Bearer 02fbdbf0-bb0e-4368-84d1-a20c198a8b36"
}