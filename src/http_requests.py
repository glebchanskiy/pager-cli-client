import requests
import urllib.request

from src.message import Message
from src.config import API_URL

def connect(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def get_all(limit: int | None) -> list[Message] | None:
    response = requests.get(
        f"http://{API_URL}/shared", params={"limit": limit} if limit is not None else None)
    if response.status_code == 200:
        messages = response.json()
        return [Message.parse_obj(m) for m in messages]
    else:
        return None


def send(message: Message):
    requests.post(url=f"http://{API_URL}/shared", data=message.json(),
                  headers={"Content-Type": "application/json"})