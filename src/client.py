from src.message import Message
from src.config import USERNAME
from src.config import API_URL

from src.http_requests import get_all
from src.http_requests import send
from src.http_requests import connect


def main():
    while True:
        command: str = input(">>> ")

        if command.startswith("@show"):
            if len(command.split()) == 2:
                print_dialog(int(command.split()[1]))
            else:
                print_dialog()
        elif command.startswith("@help"):
            print("""
ДЛЯ ОМЕЖЕК:
@show [0 < число сообщений < 100] - показать сообщения 
@help - показать сообщение для омежек
"""
            )
        else:
            send(Message(text=command, userId=USERNAME))


def start() -> None:
    print(f"Hi, {USERNAME}")
    if connect(f"http://{API_URL}/shared"):
        try:
            main()
        except KeyboardInterrupt:
            print("\nПоки 😘")
        except Exception as err:
            print("Прозошли какие-то казусы...\n" + err)
    else:
        print("Сервер недоступен")


def print_dialog(limit: int = None):
    if limit is not None:
        if limit < 1 or limit > 100:
            print("Много хочешь 🤡")
            return
    
    messages_list = get_all(limit)

    for message in messages_list:
        if message.userId == USERNAME:
            # print(f"\t\t {message.text} : <you> \n")
            print(f"[{message.text}] <- you\n")
        else:
            print(f"<{message.userId}> : {message.text}\n")
