from data import menu


user_state = {
    "language": None,
    "current_menu": "language_selection"
}

def show_menu():
    menu_name = user_state["current_menu"]

    if menu_name == "language_selection":
        print("\n"+ menu["language_selection"]["text"]["en"])
        for button in menu["language_selection"]["buttons"]:
            print(button)
        return

    language = user_state.get("language")
    current = menu.get(menu_name, {}).get("language")
    print("\n"+ current["text"])
    for button in current["buttons"]:
        print(button)


def handle_input(user_input):
    if user_input in ["Change language", "Sprache ändern"]:
        user_state["current_menu"] = "language_selection"
        user_state["language"] = None
        return

    current_menu = user_state["current_menu"]

    if current_menu == "language_selection":
        if user_input == "English":
            user_state["language"] = "en"
            user_state["current_menu"] = "main_menu"
        elif user_input == "Deutsch":
            user_state["language"] = "de"
            user_state["current_menu"] = "main_menu"
        else:
            print("Please choose: English or Deutsch")
        return

    if user_input in ["Back", "Zurück", "⬅ Back", "⬅ Zurück"] and current_menu != "main_menu":
        user_state["current_menu"] = "main_menu"
        return

    navigation = {
        "🏛 About JGU": "about_jgu",
        "About JGU": "about_jgu",
        "Über JGU": "about_jgu",
        "🎓 General Student Information": "stud_info",
        "Studierendeninfo": "stud_info",
        "🌍 International Students": "international_students",
        "Internationale Studierende": "international_students",
        "📞 Contact": "contact",
        "Kontakt": "contact"
    }

    language = user_state["language"]

    if user_input in navigation:
        user_state["current_menu"] = navigation[user_input]
    else:
        if language == "de":
            print("Bereich ist noch nicht implementiert.")
        else:
            print("Section not implemented yet.")