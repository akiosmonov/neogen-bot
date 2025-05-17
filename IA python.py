import telebot
import requests

TELEGRAM_TOKEN = "7586056221:AAGE7suhPQniEl-weK7XMbYtbn36q9A8mwU"
OPENROUTER_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text

    headers = {
        "Authorization": f"Bearer {'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'}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "Ты умный и дружелюбный ассистент."},
            {"role": "user", "content": user_text}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        bot.send_message(message.chat.id, reply)
    else:
        bot.send_message(message.chat.id, "Ошибка при обращении к ИИ.")

bot.polling()
