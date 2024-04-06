import os
import glob
import argparse

#animation names should end with - to help this process
parser = argparse.ArgumentParser(usage="Use to turn blender animations into correctly named assets for asset packing (iso_map_maker/iso games)\nMake sure blender animations are in the following order 0001:right, 0002:left, 0003:bottom, 0004:top\nFor walls this means the wall in the right/left/bottom/or top quadrant\nfor objects this refers to the direction the object is facing\n")

frame_translate = {
    "0001": "right",
    "0002": "left",
    "0003": "bottom",
    "0004": "top"
}

imgs = glob.glob("**/*.png",recursive=True)

for img in imgs:
    leaf = os.path.basename(img)
    frame = leaf.split("-")[1].split(".")[0]
    new_name = leaf.split("-")[0] +"-"+frame_translate[frame]
    os.rename(img,os.path.dirname(img)+new_name+".png")
