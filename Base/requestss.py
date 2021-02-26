import requests
from Base.session import Session
import demjson
class Requestss:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie":Session().session()
        }

    def requests_get(self,api,params):
        r = requests.get(Session().host+api,headers=self.headers, params=params)
        return r.json()


    def requests_post(self,api,data):
        r = requests.post(Session().host+api,headers=self.headers, data=demjson.encode(data))
        return r.json()


if __name__ == '__main__':
    api = "/yundeng/organization/getOrgListByParentorgid"
#     apis = "/yundeng/organization/createOrganization"
#     api1 = "/yundeng/organization/updateOrganization"
#     api2 = "/yundeng/organization/deleteOrganization"
    params = {

        "pageSize":10,
        "pageNum":1,
        "parentorgid":"700b5c90906d4cf38b2a3f06e18f645a"
    }
#
#     data = {"orgname":"xbcvb","parentorgid":"700b5c90906d4cf38b2a3f06e18f645a","orgcode":"xcbbxffffb"}
#
#     data1 = {"orgname":"第一个组织",
#              "orgcode":"qqq",
#              "parentorgid":"700b5c90906d4cf38b2a3f06e18f645a",
#              "remark":"",
#              "orgid":"e703d2b8ce3c416eb5ba86e3c7973173"
#     }
#     # a = Requestss().requests_post(apis, data)
#     # print(a)
#
#     data2 = {
#         # "orgid":a["Data"]["orgId"]
#     }
#
    print(Requestss().requests_get(api,params))
#     # print(Requestss().requests_post(api1,data1))
#     # print(Requestss().requests_post(api2,data2))



