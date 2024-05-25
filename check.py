import requests
from time import time
#from PIL import Image
import base64
"""
def base64_to_image(base64_string, output_path):
    with open(output_path, 'wb') as image_file:
        decoded_string = base64.b64decode(base64_string)
        image_file.write(decoded_string)
"""
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

cookies = {
    "connect.sid": "s%3ADZ7ifD-_7QolW81FU3c8d2Ruc1IHtO6u.eLQYpzT4sKQKXoEJHdWnJFqeEEBsi4dm9Y7iJOJ37ZU"
}
t = int(time())
re = requests.get(f"https://wemc.cc/v1/user/sign/code/?_t={t}", cookies=cookies)
if re.json()['code'] == 200:
    img = re.json()['data']
    img = img.split(",")[-1]
else:
    print("error")
    raise TimeoutError("failed to get the img")

answer=img_to_answer(img)
print(img)
#base64_to_image(img,"a.jpg")
t = int(time())
url2=f"https://wemc.cc/v1/user/sign/?code={answer}&_t={t}"
print(url2)
re=requests.get(url2,cookies=cookies)
print(re.text)
