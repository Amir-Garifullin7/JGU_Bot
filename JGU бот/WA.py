from whatsapp_chatbot_python import GreenAPIBot, Notification
from data import menu
from bot import handle_input, user_state  # show_menu пока можно не трогать

#ID_INSTANCE = "7107583832"
#API_TOKEN_INSTANCE = "89c3326f875a4821bc49c5659e537c89b93c584252b74814b4"

bot = GreenAPIBot(ID_INSTANCE, API_TOKEN_INSTANCE)


@bot.router.message()
def message_handler(notification: Notification) -> None:
    text = notification.event["messageData"]["textMessageData"]["textMessage"]

    # прогоняем ввод через lогику
    handle_input(text)

    # формируем ответ как в консоли
    menu_name = user_state["current_menu"]
    language = user_state["language"]

    if menu_name == "language_selection":
        current = menu["language_selection"]
        reply = current["text"]["en"] + "\n" + "\n".join(current["buttons"])
    else:
        current = menu[menu_name][language]
        reply = current["text"] + "\n" + "\n".join(current["buttons"])

    notification.answer(reply)


if __name__ == "__main__":
    bot.run_forever()