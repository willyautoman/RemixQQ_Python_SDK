import requests


class App:
    """
    App类用于创建和管理应用程序实例。

    属性:
    - name: 应用程序的名称，字符串类型。
    """

    def __init__(self, url: str, token: str) -> None:
        """
        类的初始化方法。

        参数:
        url: str - 提供服务的URL，从MyQQHTTPAPI内复制，格式通常应为“http://locoalhost:Port/MyQQHTTPAPI”
        token: str - 用于认证的令牌。

        """
        self.url = url
        self.token = token

    def __send_request(self, params):
        Session = requests.Session()
        result = Session.post(self.url, json=params)
        return result.json()

    def get_version(self):
        """
        获取框架版本号
        """
        params = {
            "function": "Api_GetVer",
            "token": self.token,
        }

        return self.__send_request(params)

    def get_time_stamp(self):
        """
        获取时间戳
        """
        params = {
            "function": "Api_GetTimeStamp",
            "token": self.token,
        }

        return self.__send_request(params)
