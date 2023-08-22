from tkinter import simpledialog
import pandas as pd
import imageio
import shutil
import os
from tkinter.filedialog import askdirectory
import tkinter as tk

def convert_16to8bit(main_path, dest_path):
    cwd = os.path.abspath(main_path)
    files = os.listdir(cwd)
    for file in files:
        if file.endswith('.tiff'):
            image = imageio.imread(os.path.join(main_path, file))
            image = image / 256
            image = image.astype('uint8')
            imageio.imwrite(os.path.join(dest_path, file), image)


def converting16to8_script():
    main_path = askdirectory(title='Select folder to convert tiff files')
    dest_path = askdirectory(title='Select destination folder to save files')
    convert_16to8bit(main_path, dest_path)


if __name__ == '__main__':
    converting16to8_script()