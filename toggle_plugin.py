import requests
import re
import sys

def toggle(plugin, enable):

    s = requests.Session()

    # Enter you web ui credentials here
    creds = "tommy:t0mmycat"

    login_url = f"http://{ creds }@10.0.0.2:8080/plugins"

    loginresponse = s.get(login_url)

    # Extract the session cookie from the response
    session_cookie = loginresponse.cookies['session']

    # Extract the CSRF token from the response
    csrf_token_pattern = re.compile(r'name="csrf_token" value="(\S+)"')
    csrf_token = csrf_token_pattern.search(loginresponse.text).group(1)

    toggle_url = f"http://{ creds }@10.0.0.2:8080/plugins/toggle"

    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": f"session={session_cookie}",
    "Referer": "http://10.0.0.2:8080/plugins",
    "X-Requested-With": "XMLHttpRequest"
    }

    params = {
        "enabled": "on",
        "csrf_token": csrf_token,
        "plugin": plugin
    }

    #check if we are enabling or disabling the plugin
    if enable == 1: params.pop("enabled", None)
    print(params)
    response = s.post(toggle_url, headers=headers, data=params)

    return response.text

plugin = sys.argv[1]

enable = 0

response = toggle(plugin, enable)

#if the plugin is already enabled, disable it
if response == "failed":
    enable = 1
    response = toggle(plugin, enable)

print(response)