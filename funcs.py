import requests, database, json

url = "https://shaxcoder.pythonanywhere.com"


def deploy_site(title, html, user_id):
    headers = {"Content-Type": "application/json"}
    data = {"title": title, "html": html, "password": "wp2pwshaxcoder"}
    res = requests.post(url=url+"/api/page/", headers=headers, data=json.dumps(data))
    database.create_page(user_id=user_id, url=f"{url}/page/{res.json()['pagename']}")
    print(res.text)

