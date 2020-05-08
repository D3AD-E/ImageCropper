from PIL import Image

while True:
    path = ""
    choice = input("Use path by default? y/n ")
    path = input("Input full path ")

    with Image.open(path) as image:
        print("File found!")
        width, height = image.size
        if width > 512 or height > 512:
            print("Size cannot be more than 512x512")
        print(f"Width = {width}\nHeight = {height}")
        image = image.convert("RGBA")
        pixdata = image.load()
        pixgot = list()
        for y in range(height):
            for x in range(width):
                if pixdata[x, y] != (0, 0, 0, 0):
                    pixgot.append((x, y))
        image = image.crop((pixgot[0][0], pixgot[0][1], pixgot[-1][0] + 1, pixgot[-1][1] + 1))
        image.save(path + "NEW.png", "PNG")
        width, height = image.size
        if width > 512 or height > 512:
            print("WARNING")
            print("Size is still incompatible for stickers")
        print(f"New width = {width}\nNew height = {height}")
        choice = input("Are there any more files to crop? y/n ")
        if choice == "n":
            break
