from sys import argv, exit
from PIL import Image, ImageOps

def main():
    if len(argv) != 3 or argv[1].rpartition('.')[2].lower() != argv[2].rpartition('.')[2].lower():
        exit("Invalid input")

    try:
        shirt = Image.open("shirt.png")
        before = Image.open(argv[1])
    except FileNotFoundError:
        exit("File not found")

    size = shirt.size
    before = ImageOps.fit(before, size)
    before.paste(shirt, (0, 0), shirt)
    before.save(argv[2])

if __name__ == "__main__":
    main()




