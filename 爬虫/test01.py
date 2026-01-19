import requests

# 发送请求获取网页内容
url = 'https://www.baidu.com'
response = requests.get(url)

# 打印网页内容
print(response.text)