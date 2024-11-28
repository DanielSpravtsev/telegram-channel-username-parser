from telethon import TelegramClient
from telethon.tl.types import User
import asyncio

# Введите данные API
api_id = ''
api_hash = ''
channel_id = ''  # ID канала (durov)

# Клиент
client = TelegramClient('session_name', api_id, api_hash, system_version="1.8.0 (324)")

async def collect_usernames(client, channel_id):
    try:
        participants = await client.get_participants(channel_id)
        print(f"Количество участников в канале: {len(participants)}")

        data = []
        for participant in participants:
            if isinstance(participant, User) and participant.username:
                data.append(participant.username)

        # Сохраняем usernames в файл
        with open("usernames.txt", "w", encoding="utf-8") as file:
            for username in data:
                file.write(username + "\n")

        print(f"Собрано {len(data)} usernames. Результаты сохранены в usernames.txt.")
    except Exception as e:
        print("Произошла ошибка: ", e)

# Запуск
async def main():
    await client.start(password=str(input("Введите пароль: ")))
    await collect_usernames(client, channel_id)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
