# Telegram Channel Username Scraper

## Описание

Скрипт для сбора имен пользователей из телеграм каналов в Telegram.

## Установка и запуск

### Требования

- Python 3.8 или выше
- Интернет-соединение
- Учетная запись Telegram

### Шаги установки

1. **Скачайте проект** и перейдите в его папку.

2. **Создайте виртуальное окружение**:

   ```bash
   python3 -m venv venv
   ```

3. **Активируйте виртуальное окружение**:

   - На macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - На Windows:
     ```batch
     venv\Scripts\activate
     ```

4. **Установите зависимости**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Получите данные API**:

   - Перейдите на сайт [my.telegram.org](https://my.telegram.org/apps).
   - Войдите, используя ваш номер телефона.
   - Перейдите в раздел **API Development Tools**.
   - Создайте новое приложение и получите **api_id** и **api_hash**.
   - Откройте файл `main.py` и вставьте полученные значения в соответствующие переменные.

6. **Запустите скрипт**:

   ```bash
   python main.py
   ```

   или

   ```bash
   python3 main.py
   ```

### Примечания

- **Первый запуск**: При первом запуске скрипт может запросить ввод вашего номера телефона и пароля двухфакторной аутентификации, если он установлен.
- **Сохранение данных**: Собранные имена пользователей будут сохранены в файле `usernames.txt` в той же папке.

## Структура проекта

- `main.py` — основной скрипт для сбора имен пользователей.
- `requirements.txt` — файл с зависимостями проекта.
- `README.md` — инструкции по установке и запуску.
- `usernames.txt` — файл, в который будут сохраняться собранные имена пользователей.

## Возможные проблемы

- **Ошибка `ModuleNotFoundError: No module named 'telethon'`**:

  - Убедитесь, что вы активировали виртуальное окружение (шаг 3).
  - Проверьте, что зависимости установлены правильно (шаг 4).

- **Ошибка `pip: command not found`**:

  - Убедитесь, что `pip` установлен и доступен в вашем окружении.
  - Если `pip` не установлен, обновите его командой:

    ```bash
    python -m ensurepip --upgrade
    ```
