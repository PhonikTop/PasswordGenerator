# Import the Generator class from generator module
from generator import Generator


# Define the Main_menu function
def Main_menu():
    try:
        # Instantiate a Generator object
        gen = Generator()
        # Get symbols, signs, and all symbols from the Generator object
        symbols = gen.symbols()
        signs = gen.signs()
        all_sym = gen.all_sym()

        # Print the symbols, signs, and all symbols
        print(f":We have several options for your password. Password consisting of\n" f"Latin and Cyrillic characters: {symbols}n" f"Signs: {signs}n" f"Latin and Cyrillic characters + signs: {all_sym}n")

    except Exception as e:
        # Handle exceptions and print an error message
        print(f"An error occurred: {e}. Please try again.")


# Execute Main_menu if the script is run directly
if __name__ == "__main__":
    Main_menu()
