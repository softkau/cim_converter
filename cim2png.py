import zlib
from PIL import Image
import sys, os

if len(sys.argv) < 2:
    print("No input files selected.")
    input()
    exit()

FMTS = {
    3:  "RGB",
    4: "RGBA",
}

for srcpath in sys.argv[1:]:
    pre, ext = os.path.splitext(srcpath)
    if ext != ".cim" and ext != ".CIM":
        print("input file {} has invalid extension. ignored.".format(srcpath))
        continue
    
    print("Processing {}... ".format(srcpath), end='')
    
    with open(srcpath, "rb") as fr:
        pixmap = zlib.decompress(fr.read())

    w = int.from_bytes(pixmap[:4], "big")
    h = int.from_bytes(pixmap[4:8], "big")
    fmt = int.from_bytes(pixmap[8:12], "big")

    image = Image.frombytes(FMTS[fmt], (w, h,), pixmap[12:])

    with open(pre + ".png", "wb") as fw:
        image.save(fw, format="png")

    print("Done.")

input()

