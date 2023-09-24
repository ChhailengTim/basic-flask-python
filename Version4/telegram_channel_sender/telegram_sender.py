import telebot
from session import telegram_bot_token_session

# Telegram configuration
telegram_bot_token = telegram_bot_token_session
telegram_chat_ids = ['@test158433', '@m1mac20']

# Initialize Telegram bot
bot = telebot.TeleBot(telegram_bot_token)

# Send Telegram messages to multiple users
for chat_id in telegram_chat_ids:
    try:
        bot.send_message(chat_id, "MSC Media Agency ជាក្រុមហ៊ុនមុនគេបង្អាស់ដែលផ្ដល់សេវាកម្មច្រើនបែបនិងសំបូរបែបបំផុតដែលមិនធ្លាប់មានពីមុនមក 👌ម្ចាស់អាជីវកម្ម និង អ្នកផលិតមាតិកាលើអ៊ីនធើណែត ជួបគ្នាឆាប់ៗៗៗនេះ ...")
        print(f"Telegram message sent to {chat_id} successfully.")
    except telebot.apihelper.ApiException as e:
        print(f"Failed to send Telegram message to {chat_id}. Error: {e}")
