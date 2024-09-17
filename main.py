from telethon import TelegramClient
from telethon.tl.types import User
import asyncio

# Введите данные API
api_id = ''
api_hash = ''

# Клиент
client = TelegramClient('session_name', api_id, api_hash, system_version="1.8.0 (324)")

async def parsing(client):
    dialogs = await client.get_dialogs()
    print("Диалогов на аккаунте: ", len(dialogs))
    flag = True
    data = []
    cnt_true = 0
    for i in range(0, len(dialogs)):
        if isinstance(dialogs[i].entity, User):
            try:
                username = dialogs[i].entity.username
                if username is not None:
                    data.append(username)
                    cnt_true += 1
            except Exception as e:
                print("ERROR ", e)
                print("Номер на котором остановилась работа: ", i)
                print("Успело собраться: ", cnt_true)
                flag = False
                break

    with open("usernames.txt", "a", encoding='utf-8') as file:
        for username in data:
            file.write(username + "\n")
    if flag:
        print("Успешное завершение, собрано username's: ", cnt_true)
    else:
        print("Завершение с ошибкой, за этот запуск собрано: ", cnt_true)
        print("Запустите скрипт снова с циклом, который начинается с номера: ", i)
    exit()

# Запуск
async def main():
    await client.start(password=str(input("Введите пароль: ")))
    await parsing(client)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())