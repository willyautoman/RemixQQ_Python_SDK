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
        - url (str): 提供服务的URL，格式通常应为“http://localhost:Port/MyQQHTTPAPI”。
        - token (str): 用于认证的令牌。
        - qq (str): 机器人QQ号。
        """

        self.url = url
        self.token = token
        self.qq = qq

    def __send_request(self, params: dict) -> dict:
        """
        发送请求到服务端。

        参数:
        - params (dict): 请求的参数。

        返回值:
        - dict: 服务端返回的响应数据。
        """

        Session = requests.Session()
        result = Session.post(self.url, json=params)
        return result.json()

    def get_version(self) -> str:
        """
        获取框架版本号。

        返回值:
        - str: 框架的版本号。
        """

        params = {
            "function": "Api_GetVer",
            "token": self.token,
        }
        return self.__send_request(params)

    def get_time_stamp(self) -> int:
        """
        获取当前框架内部时间戳。

        返回值:
        - int: 当前框架内部的时间戳。
        """

        params = {
            "function": "Api_GetTimeStamp",
            "token": self.token,
        }
        return self.__send_request(params)

    def log_to_myqq(self, message: str) -> dict:
        """
        在框架记录页输出一行信息。

        参数:
        - message (str): 要输出的内容。

        返回值:
        - dict: 服务端返回的响应数据。
        """

        params = {
            "function": "Api_OutPut",
            "token": self.token,
            "params": {
                "c1": message,
            }
        }
        return self.__send_request(params)

    def get_nick(self, target_qq: str) -> str:
        """
        获取指定QQ号的昵称。

        参数:
        - target_qq (str): 目标QQ号。

        返回值:
        - str: 目标QQ号的昵称。如果无法获取，则返回空字符串。
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

    def send_friend_msg(self, target_qq: str, content: str, bubble_id: int = 0) -> dict:
        """
        发送好友消息的方法。

        参数:
        - target_qq (str): 目标好友的QQ号。
        - content (str): 消息内容。
        - bubble_id (int, optional): 气泡ID，默认为0使用本来的气泡，-1为随机气泡。

        返回值:
        - dict: 服务端返回的响应数据。
        """

        params = {
            "function": "Api_SendMsgEx",
            "token": self.token,
            "params": {
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

    def send_group_message(self, target_group: str, is_anonymous: int, group_type: int, content: str,
                           bubble_id: int = 0) -> dict:
        """
        发送群组消息的函数。

        参数:
        - target_group (str): QQ群号。
        - is_anonymous (int): 是否匿名发送，0为非匿名，1为匿名。
        - group_type (int): 群组类型，2群 3讨论组 4群临时会话 5讨论组临时会话。
        - content (str): 消息的内容。
        - bubble_id (int, optional): 气泡ID，用于特定的消息样式，默认为0。

        返回值:
        - dict: 服务端返回的响应数据。
        """

        params = {
            "function": "Api_SendMsgEx",
            "token": self.token,
            "params": {
                'c1': self.qq,
                'c2': is_anonymous,
                'c3': group_type,
                'c4': target_group,
                'c5': '',
                'c6': content,
                'c7': bubble_id
            }
        }
        return self.__send_request(params)

    def get_friend_list(self) -> list:
        """
        获取好友列表。

        返回值:
        - list: 好友列表，包含好友的QQ号。如果获取失败，返回错误信息。
        """

        params = {
            "function": "Api_GetFriendList",
            "token": self.token,
            "params": {
                'c1': self.qq
            }
        }
        res = self.__send_request(params)
        if res.get('msg') == '成功':
            return res.get('data', {}).get('ret', {}).get('result', [])
        else:
            return res

    def send_group_message_json(self, target_group: str, group_type: int, json_str: str) -> dict:
        """
        向指定群组发送JSON格式的消息。

        参数:
        - target_group (str): 目标群组的ID或号码。
        - group_type (int): 群组类型，2群 3讨论组 4群临时会话 5讨论组临时会话。
        - json_str (str): 要发送的JSON格式字符串消息内容。

        返回值:
        - dict: 服务端返回的响应数据。
        """

        params = {
            "function": "Api_SendJson",
            "token": self.token,
            "params": {
                'c1': self.qq,
                'c2': 0,
                'c3': group_type,
                'c4': target_group,
                'c5': '',
                'c6': json_str
            }
        }
        return self.__send_request(params)

    def send_group_message_xml(self, target_group: str, group_type: int, xml_str: str) -> dict:
        """
        向指定群组发送XML格式的消息。

        参数:
        - target_group (str): 目标群组的ID或号码。
        - group_type (int): 群组类型，2群 3讨论组 4群临时会话 5讨论组临时会话。
        - xml_str (str): 要发送的XML格式字符串消息。

        返回值:
        - dict: 服务端返回的响应数据。
        """

        params = {
            "function": "Api_SendXml",
            "token": self.token,
            "params": {
                'c1': self.qq,
                'c2': 0,
                'c3': group_type,
                'c4': target_group,
                'c5': '',
                'c6': xml_str,
                'c7': 0
            }
        }
        return self.__send_request(params)

    def get_group_list(self) -> list:
        """
        获取群组列表。

        返回值:
        - list: 群组列表，包含群组的ID。如果获取失败，返回错误信息。
        """

        params = {
            "function": "Api_GetGroupList_B",
            "token": self.token,
            "params": {
                'c1': self.qq
            }
        }
        res = self.__send_request(params)
        if res.get('msg') == '成功':
            return res.get('data', {}).get('ret', {}).get('join', [])
        else:
            return res

    def get_group_member_list(self, target_group: str) -> list:
        """
        获取群组成员列表。

        参数:
        - target_group (str): 目标群组的ID。

        返回值:
        - list: 群组成员列表，包含群组成员的QQ号。如果获取失败，返回错误信息。
        """

        params = {
            "function": "Api_GetGroupMemberList_B",
            "token": self.token,
            "params": {
                'c1': self.qq,
                'c2': target_group
            }
        }
        res = self.__send_request(params)
        if res.get('msg') == '成功':
            member_list = res.get('data', {}).get('ret', [])
            member_list.pop()  # 假设最后一个元素是空的，根据上下文移除
            return member_list
        else:
            return res

    def get_group_admin_list(self, target_group: str) -> dict:
        """
        获取群组管理员列表。(疑似已废弃）

        参数:
        - target_group (str): 目标群组的ID。

        返回值:
        - list: 管理员列表，包含群组成员的QQ号。如果获取失败，返回错误信息。
        """
        params = {
            "function": "Api_GetAdminList",
            "token": self.token,
            "params": {
                'c1': self.qq,
                'c2': target_group
            }
        }

        return self.__send_request(params)

    def get_cookies(self) -> dict:
        """
        取得机器人网页操作用的Cookies

        返回值：
        """
        params = {
            "function": "Api_GetCookies",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }

        return self.__send_request(params)

    def get_blog_pskey(self) -> dict:
        """
        取得腾讯微博页面操作用参数P_skey
        """
        params = {
            "function": "Api_GetBlogPsKey",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }
        return self.__send_request(params)

    def get_zone_pskey(self) -> dict:
        """
        取得QQ空间页面操作用参数P_skey
        """
        params = {
            "function": "Api_GetZonePsKey",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }
        return self.__send_request(params)

    def get_group_pskey(self) -> dict:
        """
        取得QQ群页面操作用参数P_skey
        """
        params = {
            "function": "Api_GetGroupPsKey",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }
        return self.__send_request(params)

    def get_classroom_pskey(self) -> dict:
        """
        取得QQ教室页面操作用参数P_skey
        """
        params = {
            "function": "Api_GetClassRoomPsKey",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }
        return self.__send_request(params)

    def get_ten_pay_pskey(self) -> dict:
        """
        取得QQ钱包页面操作用参数P_skey
        """
        params = {
            "function": "Api_GetTenPayPsKey",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }
        return self.__send_request(params)

    def get_jubao_pskey(self) -> dict:
        """
        取得QQ举报页面操作用参数P_skey
        """
        params = {
            "function": "Api_GetJuBaoPsKey",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }

        return self.__send_request(params)

    def get_bkn(self) -> dict:
        """
        取得机器人网页操作用参数Bkn或G_tk
        """
        params = {
            "function": "Api_GetBkn",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }
        return self.__send_request(params)

    def get_bkn_32(self) -> dict:
        """
        取得机器人网页操作用参数长Bkn或长G_tk
        """
        params = {
            "function": "Api_GetBkn32",
            "token": self.token,
            "params": {
                'c1': self.qq,
            }
        }
        return self.__send_request(params)
