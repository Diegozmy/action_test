import requests

url = "https://api.mefrp.com/api/v4/auth/user/sign"
headers = {
    "Authorization": "Bearer fe4238946b8df24025097330dfde961d",
}

response = requests.post(url, headers=headers)

print(response.status_code)
print(response.text)
