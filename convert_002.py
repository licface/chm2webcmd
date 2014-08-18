from PIL import Image
import sys

im = Image.open(sys.argv[1])
bg = Image.new("RGB", im.size, (255,255,255))
bg.paste(im,im)
bg.save("out.png")