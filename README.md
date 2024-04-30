# RemixQQ_Python_SDK

给RemixQQ的Httpapi插件写的用于Python的SDK

~~要不是连API都没有能用的，我何苦自己写SDK啊！！~~

此SDk是基于MyQQ_Httpapi插件的，此插件的食用方法及下载方法参见[RemixQQ官方网站](https://www.myqqx.cc/)

## 食用方法

1. MyQQ_Httpapi的配置方法
   1. 在主界面配置端口号及Token（用于发送消息）
   ![](https://image-bed.ityun.tech/1.png)
   2. 在“回调”界面配置接收消息用的地址（重要！！！）
   ![](https://image-bed.ityun.tech/2.png)

2. 使用pip安装
```shell
pip install RemixQQ_Python_SDK
```

1. 使用以下代码进行初始化
```python
from http.server import HTTPServer, BaseHTTPRequestHandler
from remixqq_python_sdk.app import App
import json
import urllib.parse
import random
import requests
host = ('localhost', 8082) #接收消息地址（需与上方配置界面一致）
app = App('http://localhost:8081/MyQQHTTPAPI', "Token", "QQ")
class Resquest(BaseHTTPRequestHandler):
    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length'])).decode()
        datas = json.loads(datas)
        from_qun = urllib.parse.unquote(datas['MQ_fromID']) #获取消息来源群号
        msg = urllib.parse.unquote(datas['MQ_msg']) #获取消息内容
        # do something
        response = app.send_group_message("123",0,0,"test")
        print(response)

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
```
## TODO:
1. 将API完整复刻至Python
2. 实现一个包即可完成消息收发
3. 建立API文档

## Release Note
### 0.0.1（发布日期：2024年4月26日）
1. 已完成基础功能
2. 发布包至PYPI，可使用pip安装
3. 新增代办：建立API文档
4. 
