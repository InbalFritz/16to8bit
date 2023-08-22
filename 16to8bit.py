import imageio.v2 as imageio
import os
from tkinter.filedialog import askdirectory
from PIL import Image


def convert(img, target_type_min, target_type_max, target_type):
    imin = img.min()
    imax = img.max()
    a = (target_type_max - target_type_min) / (imax - imin)
    b = target_type_max - a * imax
    new_img = (a * img + b).astype(target_type)
    return new_img

def convert_6to8bit(main_path, dest_path):
    cwd = os.path.abspath(main_path)
    files = os.listdir(cwd)
    for file in files:
        if file.endswith('.tiff'):
            img_path = os.path.join(main_path, file)

            img = Image.open(img_path)
            if img.mode == "I;16":
                image = imageio.imread(img_path)
                image = image / 256
                image = image.astype('uint8')
                imageio.imwrite(os.path.join(dest_path, file), image)


def converting16to8_script():
    main_path = askdirectory(title='Select folder to convert tiff files')
    dest_path = askdirectory(title='Select destination folder to save files')
    convert_6to8bit(main_path, dest_path)


if __name__ == '__main__':
    converting16to8_script()