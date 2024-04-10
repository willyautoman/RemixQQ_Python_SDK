from remixqq_python_sdk.app import App

app = App("http://114.55.116.67:8081/MyQQHTTPAPI", "404", "1328382485")

print(app.send_group_message("920610028", 0, "只因你太美"))
