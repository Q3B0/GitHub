# -*- coding: utf-8 -*-
import httplib2
import hashlib
import time


sign_sercet = "zJwaQBQ553lHr6DfnX02WcJtZF"

t = str(int(time.time()))
status = "2"    # 热门电影=1，即将上映=2
cityId = "210"

params = {
    "uid": "",
    "v": "2015110401",
    "t": t,
    "status": status,
    "cityId": cityId,
    "imei": "89860114245102549313",
    "appkey": "9",
    "from": "0123456789",
    "appver": "5.3.0",
    "deviceid": "ffffffff-f5cf-efcc-ffff-ffff868b5e5e"
}

# 对 KV 进行按头字母排序
params_str = ""
keys = params.keys()
keys.sort(reverse=False)
for key in keys:
    params_str += key + "=" + params[key] + "&"
params_str = params_str[:-1]

# 取 sign 值
h = hashlib.md5()
h.update(sign_sercet + params_str)
sign = h.hexdigest().upper()

post_body = "sign=" + sign + "&" + params_str

# 输出添加签名后的 Http Post Body
print post_body

headers = {
    "channelId": "9",
    "token": "",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "Keep-Alive",
    "User-Agent": ""}

httpclent = httplib2.Http()
content = httpclent.request("http://androidcgi.wepiao.com/movie/list", 'POST', headers=headers, body=post_body)[1]
print content