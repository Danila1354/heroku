import requests
import json
token='7e74dd8dca15fa28559fccce5a8798e6bc33591cb49f94d993ce36f7d230a601c0d39bf31f0808102f7d1'
url = f'https://api.vk.com/method/wall.get?domain=wave_number_one&count=500&access_token={token}&v=5.81'
list_r = []
def get_wall(date):
    r = requests.get(url=url)
    info = json.loads(r.text)
    with open('1.json', 'w', encoding='utf-8') as file:
        json.dump(info, file, indent=2, ensure_ascii=False)
    posts=info.get('response').get('items')
    try:
        for post in posts:
            if 'Расписание' in post.get('text') and date in post.get('text'):
                post_att = post.get('attachments')
                photo = post_att[1].get('photo').get('sizes')[-1].get('url')
    except Exception:
        photo='Расписание еще не выложили'
    try:
        return photo
    except Exception:
        return 'Расписание еще не выложили'