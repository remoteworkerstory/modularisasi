import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'success! response = {response.status_code}')
        print(f'content \n{response.text}')
    else:
        print(f'aduh, ada error{response.status_code}')

except Exception as e:
    print(f'ada error {e}')
