import requests

resp = requests.get('http://192.168.1.227:8080/area?a=100&b=350&form=rectangle')
resp = requests.get('http://192.168.1.227:8080/area?h=5&b=5&form=triangle')
print(resp.status_code, resp.text)

resp = requests.get('http://192.168.1.227:8080/area?a=5&b=7&form=rectangle')
print(resp.status_code, resp.text)

resp = requests.get('http://192.168.1.227:8080/area?a=5&form=square')
print(resp.status_code, resp.text)



resp = requests.get('http://192.168.1.227:8080/sum')
print(resp.status_code, resp.text)

resp = requests.delete('http://192.168.1.227:8080/sum')
print(resp.status_code, resp.text)

resp = requests.get('http://192.168.1.227:8080/sum')
print(resp.status_code, resp.text)



resp = requests.get('http://192.168.1.227:8080/area?h=5&b=6&form=triangle')
print(resp.status_code, resp.text)

resp = requests.get('http://192.168.1.227:8080/sum')
print(resp.status_code, resp.text)