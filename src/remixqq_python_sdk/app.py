import requests


class App:
    """
    App类用于创建和管理应用程序实例。

    属性:
    - name: 应用程序的名称，字符串类型。
    """

    def __init__(self, url: str, token: str, qq: str) -> None:
        """
        类的初始化方法。

        参数:
        url: str - 提供服务的URL，从MyQQHTTPAPI内复制，格式通常应为“http://locoalhost:Port/MyQQHTTPAPI”
        token: str - 用于认证的令牌。
        qq: str - 机器人QQ
        """
        self.url = url
        self.token = token
        self.qq = qq

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
        获取当前框架内部时间戳
        """
        params = {
            "function": "Api_GetTimeStamp",
            "token": self.token,
        }

        return self.__send_request(params)

    def log_to_myqq(self, message: str):
        """
        在框架记录页输出一行信息

        参数:
        message (str): 输出的内容
        """
        params = {
            "function": "Api_OutPut",
            "token": self.token,
            "params": {
                "c1": message,
            }
        }
        return self.__send_request(params)

    def get_nick(self, target_qq: str):
        """
    获取指定QQ号的昵称。

    参数:
    target_qq (str): 目标QQ号。

    返回值:
    str: 目标QQ号的昵称。如果无法获取，则返回空字符串。
    """
        params = {
            "function": "Api_GetNick",
            "token": self.token,
            "params": {
                "c1": self.qq,
                "c2": target_qq
            }
        }
        return self.__send_request(params)

    def send_friend_msg(self, target_qq: str, content: str, bubble_id: int = 0):
        """
    发送好友消息的方法

    参数:
    - target_qq (str): 目标好友的QQ号
    - content (str): 消息内容
    - bubble_id (int): 气泡ID，默认为0使用本来的气泡，-1为随机气泡

    返回值:
    无
    """
        params = {
            "function": "Api_SendMsgEx",
            "token": self.token,
            'params': {
                'c1': self.qq,
                'c2': 0,
                'c3': 1,
                'c4': '',
                'c5': target_qq,
                'c6': content,
                'c7': bubble_id
            }
        }
        return self.__send_request(params)

    def send_group_message(self, target_group: str, is_annoymous: int, content: str, bubble_id: int = 0):
        """
    发送好友消息的方法

    参数:
    - target_group (str): 目标群的QQ号
    - content (str): 消息内容
    - bubble_id (int): 气泡ID，默认为0使用本来的气泡，-1为随机气泡

    返回值:
    无
    """
        params = {
            "function": "Api_SendMsgEx",
            "token": self.token,
            'params': {
                'c1': self.qq,
                'c2': is_annoymous if is_annoymous not in [0, 1] else 0,
                'c3': 2,
                'c4': target_group,
                'c5': '',
                'c6': content,
                'c7': bubble_id
            }
        }
        return self.__send_request(params)