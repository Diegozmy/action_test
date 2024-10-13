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
        "request_url": "http://api.tanshuapi.com/api/ocr_general/v1/index",
        "method": "get",
        "params": '{"img":"' + img + '"}'
    }

    re = requests.post("https://www.tanshuapi.com/index/api/apiDebug", json=data)

    equation = eval(re.json()['response'])['data']['list'][0].replace("\\", "").split('=')[0]
    print(equation)
    answer = eval(equation)
    print(answer)
    return answer

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
