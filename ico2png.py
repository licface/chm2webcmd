#from cStringIO import StringIO
import StringIO
import Image.Image as Image
import urllib
import sys
import os
import ImageMath

def convert(path):
    from PIL import Image

    out = os.path.splitext(path)[0] + ".png"
    im = Image.open(path)
    bg = Image.new("RGB", im.size, (255,255,255))
    bg.paste(im,im)
    bg.save(out)

def convert2(path):
    image=Image.open(path)
    out = os.path.splitext(path)[0] + ".png"
    non_transparent=Image.new('RGBA', image.size, (255,255,255,255))
    non_transparent.paste(image,(0,0),image)
    #non_transparent.paste(image,image)
    non_transparent.save(out)

def _to_png(path):
    for infile in sys.argv[1:]:
        outfile = os.path.splitext(infile)[0] + ".png"
        if infile != outfile:
            try:
                im = Image.open(infile)
                im = im.convert("RGBA")
                datas = im.load()

                for i in xrange(im.size[1]):
                    for x in xrange(im.size[0]):
                        if datas[x, i] == (255, 255, 255, 255):
                            #print "i =", i
                            #print "x =", x
                            datas[x, i] = (255, 255, 255, 0)
                
                im.save(outfile, "PNG")
            except IOError:
                print "cannot create thumbnail for", infile


def to_png(path):
    for infile in sys.argv[1:]:
        outfile = os.path.splitext(infile)[0] + ".png"
        if infile != outfile:
            try:
                im = Image.open(infile)
                im = im.convert("RGBA")
                datas = im.getdata()
                print "datas =", datas
                newData = []
                for i in datas:
                    if i[0] == 255 and i[1] == 255 and i[2] == 255:
                        print "i =", i
                        newData.append((255, 255, 255, 0))
                    else:
                        newData.append(i)
                im.putdata(newData)
                im.save(outfile, "PNG")
            except IOError:
                print "cannot create thumbnail for", infile

def distance2(a, b):
    return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2])

def makeColorTransparent(image, color, thresh2=0):
    image = image.convert("RGBA")
    red, green, blue, alpha = image.split()
    image.putalpha(ImageMath.eval("""convert(((((t - d(c, (r, g, b))) >> 31) + 1) ^ 1) * a, 'L')""",
        t=thresh2, d=distance2, c=color, r=red, g=green, b=blue, a=alpha))
    return image


if __name__ == "__main__":
    #_to_png(sys.argv[1])
    #_topng(sys.argv[1])
    #makeColorTransparent(Image.open(sys.argv[1]), (255, 255, 255)).save(sys.argv[2]);
    convert(sys.argv[1])
    #convert2(sys.argv[1])