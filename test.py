from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('font/GreatVibes-Regular.ttf')
left, top, right, bottom = font.getbbox("Hello world")
width, height = right - left, bottom - top

im = Image.new("RGB", (100, 100))
draw = ImageDraw.Draw(im)
width = draw.textlength("Hello world")

left, top, right, bottom = draw.multiline_textbbox((0, 0), "Hello\nworld")
width, height = right - left, bottom - top
