import requests_html

url = "http://whatsmyuseragent.com/"
session = requests_html.HTMLSession()


headers = {
    'User-Agent':'Mozilla/22.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
}
r = session.get(url, headers=headers)

user_agent_element = r.html.find('.user-agent', first=True)

print('Your User Agent is:')
print(user_agent_element.text)