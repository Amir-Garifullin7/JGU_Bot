from bot import show_menu, handle_input

if __name__ == "__main__":
    while True:
        show_menu()
        user_input = input("> ")
        handle_input(user_input)