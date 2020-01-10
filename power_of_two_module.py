import os
import sys

from PIL import Image
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-p', '--raw_path')
parser.add_argument('-s', '--size')
args = parser.parse_args()

RAW_PATH = args.raw_path

if __name__ == '__main__':
    filepaths = [os.path.join(RAW_PATH, "asphalt", i) for i in os.listdir(RAW_PATH + "/asphalt")]

    size = int(args.size)
    print(filepaths)

    for file in filepaths:
        img = Image.open(file)
        img = img.resize(size=(size, size))
        img.save(fp=file)
