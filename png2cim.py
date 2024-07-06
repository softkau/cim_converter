import zlib
import numpy as np
from PIL import Image
import sys, os, struct



if len(sys.argv) < 2:
    print("No input files selected.")
    input()
    exit()

def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False


for srcpath in sys.argv[1:]:
    pre, ext = os.path.splitext(srcpath)
    if ext != ".png" and ext != ".PNG":
        print("input file {} has invalid extension. ignored.".format(srcpath))
        continue

    print("Processing {}... ".format(srcpath), end='')

    image = Image.open(srcpath)
    
    if has_transparency(image):
        image = image.convert("RGBA")
        fmt = 4
    else:
        image = image.convert("RGB")
        fmt = 3

    w, h = image.size

    buf = np.zeros(12).astype(np.uint8)
    struct.pack_into('>I', buf, 0, w)
    struct.pack_into('>I', buf, 4, h)
    struct.pack_into('>I', buf, 8, fmt)

    pix = bytearray(np.array(image).astype(np.uint8))
    buf = np.concatenate((buf, pix), axis=0).astype(np.uint8)
    buf2 = zlib.compress(buf)

    with open(pre + ".cim", "wb") as fw:
        fw.write(buf2)

    print("Done.")

input()
