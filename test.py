from app import App

app = App("http://192.168.3.89:8081/MyQQHTTPAPI", "404")

print(app.get_time_stamp())
