from Base.requestss import Requestss
from Base.mysal import Connect_mysql
#新增公告
# a = input("请输入是否弹框，1需要弹框，0不需要弹框,不填默认为需要弹框：")
# b = input("请输入公告标题：")
# api = "/yundeng/notice/add"
#
# params = {
#     "columnId":149,
#     "isNewUserVisible":0,
#     "isPopupWindow":0,
#     "noticeContent":"<p>erwereret</p>",
#     "noticeState":1,
#     "noticeTargets":[{"scopeType":3,"targetId":12431,"targetName":"乐丹"}],
#     "noticeTitle":"test09",
#     "scopeType":1
#     }
#
# new = Requestss().requests_post(api, params)
#
# print(new)
#撤回公告
spl = "SELECT * FROM `notice`WHERE `notice_state` = 1 AND `tenant_id` = 42 AND `is_deleted`= 0 AND `creator_id` = 13454"
notice_id01 = Connect_mysql().queryAll(spl)
for i in range(len(notice_id01)):
    a = notice_id01[i][0]
    api = "/yundeng/notice/batchUpdateState"
    params = {
        "noticeIds":[a],
        "noticeState":"2"
    }
    batch = Requestss().requests_post(api, params)
    print(batch)

#删除公告
spl = "SELECT * FROM `notice`WHERE `notice_state` = 2 AND `tenant_id` = 42 AND `is_deleted`= 0 AND `creator_id` = 13454"
notice_id02 = Connect_mysql().queryAll(spl)
for i in range(len(notice_id02)):
    a = notice_id02[i][0]
    api = "/yundeng/notice/batchDelete"
    params = {
        "noticeIds": [a],
    }
    delete = Requestss().requests_post(api, params)
    print(delete)