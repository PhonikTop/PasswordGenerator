from generator import Generator


def Main_menu():
    try:
        gen = Generator()
        symbols = gen.symbols()
        signs = gen.signs()
        all_sym = gen.all_sym()

        print(f"{symbols}\n" f"{signs}\n" f"{all_sym}\n")

    except Exception as e:
        print(f"Произошла ошибка: {e}. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    Main_menu()
