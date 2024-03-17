import os
try:
    import base64
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install base64")


token = 'Your Bot Token is Here!'  # Put your Bot's Token
new_banner_file = open('./Forex.gif', 'rb')  # Path to your new avatar file in this case Rick-Roll is our example
new_banner = base64.b64encode(new_banner_file.read()).decode('utf-8')
new_banner_file.close()

headers = {
    'Authorization': f'Bot {token}',
    'Content-Type': 'application/json'
}

payload = {
    'banner': f'data:image/gif;base64,{new_banner}'
}

url = 'https://discord.com/api/v10/users/@me'

try:
    response = requests.patch(url, headers=headers, json=payload)

    if response.ok:
        print("Banner Updated Successfully!")
    else:
        print("Failed to Update Banner:", response.reason)
        print("Response body:", response.text)

except Exception as e:
    print("There is an Error here:", e)
