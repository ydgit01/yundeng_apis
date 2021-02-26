import requests
import demjson

a = {"username":"yuedantestadmin","password":"2493f190d57de99da0ba181cf5acc191","tenantCode":"2569f3427138b8fc16a6da2f02178aa5"}
f = {"username":"yuedan01","password":"90BAFFC9BFF2D4C7980B95B9D7F23030","tenantCode":"2569f3427138b8fc16a6da2f02178aa5"}
b ={
    "Content-Type":"application/json",

"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
proxies={'http':'http://47.111.238.207:18082'}
r = requests.post("http://yundeng-console.common.aliyun.com/api/login",data=demjson.encode(f),headers =b,proxies=proxies)
c = r.json()["Data"]
print(c)

d = {
    "pageSize":10,
    "pageNum":1,
    "parentorgid":"700b5c90906d4cf38b2a3f06e18f645a"
}

headers = {
"Content-Type":"application/json;charset=UTF-8",
    "Cookie":print()
}
r = requests.get("http://yundeng-console.common.aliyun.com/yundeng/organization/getOrgListByParentorgid",headers =headers,params=d)
print(r.json())


