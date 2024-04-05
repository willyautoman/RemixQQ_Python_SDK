from remixqq_python_sdk.app import App

app = App("http://192.168.3.89:8081/MyQQHTTPAPI", "404","1328382485")

print(app.send_friend_msg("1127738407", "测试消息"))
