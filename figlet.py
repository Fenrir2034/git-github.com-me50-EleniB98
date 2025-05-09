from pyfiglet import Figlet
import sys

def print_error_message():
    print("Invalid usage")
    sys.exit(1)

def main():
    if len(sys.argv) == 1:
        font_name = Figlet().getFonts()[0]
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font_name = sys.argv[2]
        if font_name not in Figlet().getFonts():
            print_error_message()
    else:
        print_error_message()

    figlet = Figlet(font=font_name)

    text = input("Enter text: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()

