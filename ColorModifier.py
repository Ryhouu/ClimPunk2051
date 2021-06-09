from PIL import Image
import sys
import os

def to_white (r, g, b, a):
    return (255 - r, 255 - g, 255 - b, a)

def to_lime (r, g, b, a) :
    return (124 + r, 132 + g, 62 + b, a)

def modify (src, dest_src, func) :
    img = Image.open(src).convert('RGBA')
    pxdata = img.load()

    for x in range(img.size[0]) :
        for y in range(img.size[1]) :
            (r, g, b, a) = pxdata[x, y]
            pxdata[x, y] = func(r, g, b, a)
    
    img.save(dest_src)

path = os.path.join(os.getcwd(), r'assets\map_ele')
for f in os.listdir(path) :
    src = os.path.join(path, f)
    fname, ftype = os.path.splitext(f)[0: 2]
    if ftype == '.png' and '_w' not in fname and '_h' not in fname:
        dsrc_white = os.path.join(path, fname + '_w' + ftype)
        modify(src, dsrc_white, to_white)
        dsrc_hovered = os.path.join(path, fname + '_h' + ftype)
        modify(src, dsrc_hovered, to_lime)