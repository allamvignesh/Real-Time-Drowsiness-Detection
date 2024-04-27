import requests
import geocoder

USER = os.environ['PUSHOVER_USER_ID']
API = os.environ['PUSHOVER_API_TOKEN']

def send_message():
    g = geocoder.ip('me')
    msg = f"Person may be sleepy at {g.latlng}"
    payload = {"message": msg, "user": USER, "token": API }
    r = requests.post('https://api.pushover.net/1/messages.json', data=payload, headers={'User-Agent': 'Python'})
    return r