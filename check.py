import requests
from time import time,sleep
from random import randint

# 生成一个5到10之间的随机延迟时间（秒）
delay = randint(0, 1200)

# 输出延迟时间
print("延迟时间为 {} 秒".format(delay))

# 进行延迟
sleep(delay)
print("延迟结束，继续执行下面的代码")

def img_to_answer(img):
    data = {
        "key": "be78ef0b73439d6b5f46f60eec95a372",
        "expiration": 60,
        "image": img
    }
    re = requests.post(f"https://api.imgbb.com/1/upload", data=data)
    img_url= re.json()["data"]["url"]
    url = "https://ai.baidu.com/platform/demo/red/rest/2.0/ocr/v1/general_basic"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://ai.baidu.com",
        "Connection": "keep-alive",
        "Referer": "https://ai.baidu.com/tech/ocr/general",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Cookie": "BAIDUID=215EDB122F4C0E33F64C5BFE0D808268:SL=0:NR=10:FG=1; BIDUPSID=D9FF683D30E338B2F8D8E16C3F261466; PSTM=1683717455; MCITY=-289^%^3A; H_WISE_SIDS=60451_60854_60887_60875; H_PS_PSSID=60854_61008_61027_61024; BDUSS=JGdTRTYWpMMnI1bGh-eXdFRlJ2WGVTTDNUbVBCbVNZbTZaRTdzY0hnVW1QVXhuSVFBQUFBJCQAAAAAAQAAAAEAAACVTG82ZGllZ2~Vxdz41LQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACawJGcmsCRnU3; Hm_lvt_8b973192450250dd85b9011320b455ba=1720606597; BA_HECTOR=0005a0808k018ka0ah052ga1asjpfg1ji91m41v; ZFY=Z3a932vlAZoaEMgWrWLokcxbmHsWi:BzXUEykSGaKn0E:C; delPer=0; PSINO=5; BCLID=10628181808466126898; BCLID_BFESS=10628181808466126898; BDSFRCVID=PB_OJeC62RjO1UbJ5WjehURJYT0NRkTTH6q2xYDfkolWLYvOUSFgEG0Pzx8g0KubRyJSogKK0eOTHvFF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; BDSFRCVID_BFESS=PB_OJeC62RjO1UbJ5WjehURJYT0NRkTTH6q2xYDfkolWLYvOUSFgEG0Pzx8g0KubRyJSogKK0eOTHvFF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; H_BDCLCKID_SF=tRAOoC8ytDvjDb7GbKTD-tFO5eT22-usKaRi2hcH0KLKfI5YjJJxy6LiMRJ3LljZyGPj2fooQUb1MRjvBU6ILRQbLfDtyMRjQHb7oq5TtUJSeCnTDMRhqqJXqqjyKMnitIT9-pnK3qQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02JKKuD6_aD5obDaAs5-7ybCPXLn58Kb5_f5rnhPF3KfjbXP6-35KH3K6ZBbPbWD5Rj4jd3q5kWt-Uypb75h37JDFeQPc-2-cvO-oO065d-to324oxJpOE5JbMopvaKj6nHfnvbURvD-Lg3-7q0f5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-j5JIEoK8hJII2hCKr-PvE-PnH-fv0hRQXHD7yWCvx0f7cOR5Jj65CMxRL3f5ZtlbB5CbPbqcwQIJFVRv23MA-KjDbWtOha-RQQ2JkLq7GLhQJsq0x0b6We-bQypoaQJcZLKOMahkM5l7xO-QDQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3WjjISKx-_tj-ffx5; H_BDCLCKID_SF_BFESS=tRAOoC8ytDvjDb7GbKTD-tFO5eT22-usKaRi2hcH0KLKfI5YjJJxy6LiMRJ3LljZyGPj2fooQUb1MRjvBU6ILRQbLfDtyMRjQHb7oq5TtUJSeCnTDMRhqqJXqqjyKMnitIT9-pnK3qQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02JKKuD6_aD5obDaAs5-7ybCPXLn58Kb5_f5rnhPF3KfjbXP6-35KH3K6ZBbPbWD5Rj4jd3q5kWt-Uypb75h37JDFeQPc-2-cvO-oO065d-to324oxJpOE5JbMopvaKj6nHfnvbURvD-Lg3-7q0f5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-j5JIEoK8hJII2hCKr-PvE-PnH-fv0hRQXHD7yWCvx0f7cOR5Jj65CMxRL3f5ZtlbB5CbPbqcwQIJFVRv23MA-KjDbWtOha-RQQ2JkLq7GLhQJsq0x0b6We-bQypoaQJcZLKOMahkM5l7xO-QDQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3WjjISKx-_tj-ffx5; RT=""z=1&dm=baidu.com&si=39a0deaa-2bb8-4ee1-a7f0-4eb4a5426f5f&ss=m2ylo5cg&sl=7&tt=1ncn&bcn=https^%^3A^%^2F^%^2Ffclog.baidu.com^%^2Flog^%^2Fweirwood^%^3Ftype^%^3Dperf&ld=613j""; CAMPAIGN_TRACK=30a63b59ca0f13d5427864d6a96aa9e4c4e6415f4e95727f; bce-userbind-source=PASSPORT; ucbearer-clientid=; bce-login-userid=; bce-device-token=; bce-ctl-client-cookies=""BDUSS,bce-passport-stoken,bce-device-cuid,bce-device-token,BAIDUID""; bce-auth-type=PASSPORT; SIGNIN_UC=; bce-passport-stoken=ad8891861cee47c16adc7b379090651879772a846fad307d820a0c35bd7b9638; __cas__id__285=; bce-device-cuid=; __cas__rn__=; bce-user-info=2024-11-01T18:40:40Z^|7a84031fa6e5ca04a1520a6a2a49504e; bce-ctl-sessionmfa-cookie=bce-session; ucbearer-token=; bce-session=19a510a7f34347ddb8ef01b12ebbbeec5463be77d75549d5bea1f4605ce2fb77^|ff22f59b1ec4504281da75fc350166e7; bce-verify-status=; bce-login-type=PASSPORT; CAMPAIGN_TRACK_TIME=2024-11-01+18^%^3A37^%^3A48; __cas__st__285=; bce-login-expire-time=""2024-11-01T11:10:40Z^|9f972267e2f01ef4e5b899ccbeaccc30""; ucbearer-ucid=; ucbearer-devicecode=; bce-login-display-name=diego^%^E5^%^BC^%^A0^%^E8^%^8C^%^97^%^E6^%^BA^%^90; bce-sessionid=001ef1eb4a559f54206897046d39643db50; bceAccountName=PASSPORT:5208231061; loginUserId=5208231061"
    }

    data = {
        "detect_direction": "false",
        "language_type": "CHN_ENG",
        "url": img_url
    }

    response = requests.post(url, headers=headers, data=data)

    ans= response.json()["result"]["words_result"][0]["words"].split('=')[0]
    print(ans)
    return eval(ans)

def get_cookies():
    t = int(time())
    data = {"email": "2325857342@qq.com",
            "password": "zmy20090622"}
    re = requests.post(f"https://wemc.cc/v1/auth/login/?_t={t}", json=data)
    print(re.text)
    return re.cookies

cookies = get_cookies()
t = int(time())
re = requests.get(f"https://wemc.cc/v1/user/sign/code/?_t={t}", cookies=cookies)
if re.json()['code'] == 200:
    img = re.json()['data']
    img = img.split(",")[-1]
else:
    print("error")
    raise TimeoutError("failed to get the img")

answer=img_to_answer(img)
#print(img)
#base64_to_image(img,"a.jpg")
t = int(time())
url2=f"https://wemc.cc/v1/user/sign/?code={answer}&_t={t}"
print(url2)
re=requests.get(url2,cookies=cookies)
print(re.text)

data={"day":1}
re = requests.post(f"https://wemc.cc/v1/ists/renew/?_t={t}", cookies=cookies,json=data)
print(re.json())

url="https://api.v2.rainyun.com/user/reward/tasks"
headers = {"x-api-key":"b71UnUTO59EXJupt3YZgawpZkOw0D33P"}
data={"task_name":"每日签到"}
response = requests.post(url, headers=headers, json=data)
print(response.json())
