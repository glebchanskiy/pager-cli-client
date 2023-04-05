import requests
import urllib.request

from src.message import Message
from src.config import API_URL

TOKEN = None


def get_all(limit: int | None) -> list[Message] | None:
    response = requests.get(
        f"http://{API_URL}/shared",
        params={"limit": limit} if limit is not None else None,
        headers={"Authorization": f"Bearer {TOKEN}"})

    if response.status_code == 200:
        messages = response.json()
        return [Message.parse_obj(m) for m in messages]
    else:
        return None


def send(message: Message):
    requests.post(url=f"http://{API_URL}/shared",
                  data=message.json(),
                  headers={
                      "Content-Type": "application/json",
                      "Authorization": f"Bearer {TOKEN}"
                  })


def login(username: str, password: str) -> bool:
    response = requests.post(
        f"http://{API_URL}/login",
        headers={
            "Content-Type": "application/json"
        },
        json={
            "username": username,
            "password": password
        }
    )

    if response.status_code == 404:
        return False
    elif response.status_code != 401:
        messages = response.json()
        global TOKEN
        TOKEN = messages["token"]
        return True
    else:
        return False
