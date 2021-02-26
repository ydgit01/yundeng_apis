import requests
import demjson
import json
from Base.read_ips import Read_url
class Session:
    def __init__(self):

        self.login_data = Read_url().get_url("YueDan01")

        self.requests_headers ={
            "Content-Type":"application/json",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9"
        }


        self.proxies= Read_url().get_url("Proxies")

        self.host = Read_url().get_url("YunDengUrl")

    def session(self):
        response = requests.post(self.host+"/api/login", data=demjson.encode(self.login_data), headers=self.requests_headers,proxies=self.proxies)
        result = json.loads(response.content.decode(encoding='utf8'))
        return result["data"]


print(Session().session())


