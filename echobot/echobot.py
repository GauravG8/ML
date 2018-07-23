import config
import requests

BASE_URL = "https://api.telegram.org/bot{}".format(config.bot_token)


def receive_message(msg):
    # Receive message from telegram and extract text and chat_id
    try:
        message = str(msg["message"]["text"])
        chat_id = msg["message"]["chat"]["id"]
        return message, chat_id
    except Exception as e:
        print(e)
        return None, None


def handle_message(message):
    # Handle and process message in this function. In this case, send the message back
    message = message[::-1]
    return message


def send_message(message, chat_id):
    # Send message with text and chat_id to telegram
    data = {"text": message.encode("utf-8"), "chat_id": chat_id}
    url = BASE_URL + "/sendMessage"
    try:
        response = requests.post(url, data).content
    except Exception as e:
        print(e)


def run(message):
    try:
        message, chat_id = receive_message(message)
        response = handle_message(message)
        send_message(response, chat_id)
    except Exception as e:
        print(e)
