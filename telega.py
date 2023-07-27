import json
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "6576899651:AAFFy7oTQJbeOXuKx2zCFrvd_6l5RsbAQU4"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    """
    Обработчик команды /start.

    Отправляет приветственное сообщение пользователю.

    Parameters:
        update (telegram.Update): Обновление от Telegram с информацией о событии.
        context (telegram.ext.CallbackContext): Контекст для взаимодействия с другими командами.

    Returns:
        None
    """
    user = update.message.from_user
    update.message.reply_text(f"Привет, {user.first_name}!")

    # Запись данных о пользователе
    save_user_data(user)

def help(update, context):
    """
    Обработчик команды /help.

    Отправляет сообщение с описанием функциональности бота.

    Parameters:
        update (telegram.Update): Обновление от Telegram с информацией о событии.
        context (telegram.ext.CallbackContext): Контекст для взаимодействия с другими командами.

    Returns:
        None
    """
    user = update.message.from_user
    update.message.reply_text("Я бот, который повторяет")

    # Запись данных о пользователе
    save_user_data(user)

def echo(update, context):
    """
    Обработчик текстовых сообщений.

    Повторяет текстовое сообщение пользователя.

    Parameters:
        update (telegram.Update): Обновление от Telegram с информацией о событии.
        context (telegram.ext.CallbackContext): Контекст для взаимодействия с другими командами.

    Returns:
        None
    """
    user = update.message.from_user
    text = update.message.text
    update.message.reply_text(f"Ты написал: {text}")

    # Запись данных
    save_user_data(user)

def save_user_data(user):
    """
    Сохраняет данные о пользователе в JSON-файл.

    Parameters:
        user (telegram.User): Объект, содержащий информацию о пользователе.

    Returns:
        None
    """
    user_data = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username
    }

    with open("user_data.json", "w") as f:
        json.dump(user_data, f, ensure_ascii=False)

def unknown(update, context):
    """
    Обработчик неизвестных команд.

    Отправляет сообщение с информацией о непонятной команде.

    Parameters:
        update (telegram.Update): Обновление от Telegram с информацией о событии.
        context (telegram.ext.CallbackContext): Контекст для взаимодействия с другими командами.

    Returns:
        None
    """
    update.message.reply_text("Неизвестная команда")

def main():
    """
    Основная функция для запуска бота.

    Создает и настраивает Updater, добавляет обработчики команд и сообщений,
    запускает процесс получения обновлений от Telegram.

    Returns:
        None
    """
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
