import yaml

class Read_url:

    def get_url(self,param):

        data = yaml.load(open('D:\\yundeng_apis\\Data\\Ips','r',encoding="utf-8"), Loader=yaml.FullLoader)

        return data[param]


print(Read_url().get_url("YueDanTestAdmin"))
