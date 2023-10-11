from PIL import Image
import numpy as np
import os
import sys

def count_dark_pixels(path_to_file):
    char_image = Image.open(path_to_file)
    char_image = char_image.convert("L")
    pixel_data = np.array(char_image)
    dark_pixels = np.sum(pixel_data < 200)
    char_image.close()
    
    return dark_pixels

def write_to_file(pixels_list):
    with open('char_pixel_map.txt', 'w') as file:
        for i in range(len(pixels_list)):
            file.write(f"{pixels_list[i][0]} {pixels_list[i][1]}\n")

DIRECTORY_PATH = r'C:\Users\antho\OneDrive\Documents\Coding\Python\ASCII Art\char_images'
FILE_LIST = os.listdir(DIRECTORY_PATH)

def main():
    pixels_list = []
    for file_name in FILE_LIST:
        if os.path.isfile(os.path.join(DIRECTORY_PATH, file_name)):
            path = DIRECTORY_PATH + f'\{file_name}'
            pixels_list.append([count_dark_pixels(path), file_name[0]])

    """
    NOTE: Use the w_on_b option when running this code to create the pixel
    map for white text on a black background. Run the code with no options
    to leave it for black text on a white background.
    """
    try:
        if sys.argv[1] and sys.argv[1] == 'w_on_b':
            for i in range(len(pixels_list)):
                pixels_list[i][0] = abs(255-pixels_list[i][0])
    except:
        pass

    pixels_list.sort(key=lambda pair: pair[0])

    write_to_file(pixels_list)

if __name__ == "__main__":
    main()