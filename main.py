from PIL import Image, ImageFont, ImageDraw

FontFile = ImageFont.truetype(r"font/GreatVibes-Regular.ttf", 80)
FontColor = "#00597D"
template = Image.open(r'templates/PUDSCERT.png')
WIDTH, HEIGHT = template.size


def makeCertificates(name):
    imageSource = Image.open(r'templates/PUDSCERT.png')
    draw = ImageDraw.Draw(imageSource)

    left, top, right, bottom = FontFile.getbbox(name)
    nameWidth, nameHeight = right - left, bottom - top

    draw.text(((WIDTH - nameWidth) / 2, (HEIGHT - nameHeight) / 2 - 30), name, fill=FontColor, font=FontFile)
    imageSource.save("./output/" + name + ".png")
    print('Saving Certificate of:', name)


def read_names(file_path):
    with open(file_path, 'r') as file:
        names = file.read().splitlines()
    return names


if __name__ == "__main__":
    names = read_names('names.txt')
    for name in names:
        makeCertificates(name)

    print(len(names), "certificates done.")
