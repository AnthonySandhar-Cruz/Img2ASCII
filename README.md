# Img2ASCII
A simple Python app written with Tkinter to convert images to ASCII art.

## Generate Images of ASCII Characters
In the ASCII_image_generate.py file, you can change which ASCII characters you want to use along with the font you want the characters to be in. This file will generate images of each ASCII characters. Place these images into a seperate folder once the code is complete.

## Sort ASCII Characters
The ASCII_sort.py file counts the number of dark pixels in each of the images of the ASCII characters generated in the previous step. Make sure to enter the path to the folder containing the images from the previous step into this file so it correctly finds the files. Ensure the ASCII character images are the only files in this folder. The output of this program is a text file called char_pixel_map.txt containing the ASCII characters and a number up to 255 indicating how dark the ASCII character appears. By default, it is sorted to display images with black text on a white background. Using the argument w_on_b when runnning the Python file will generate the text file for white text on a black background instead. A char_pixel_map.txt file is included in this repository. This was made using the Fira Code font, and was intended to be displayed with black text on a white background.

## Main App
The ImageToASCII.py file is the Tkinter GUI for choosing image files and converting the file to ASCII art. This can be turned into an executable file using 
```
pyinstaller --onefile --noconsole ImageToASCII.py
```
Note that the dimensions of the inputted image are kept in the conversion process. This means every pixel is turned into an ASCII character. It is recommended to reduce the image size before inputting it into the program. The output file will be saved to your downloads.

## How it Works
The char_pixel_map.txt file is turned into a dictionary assigning each ASCII character a value from 0 to 255 based on how many black pixels appear in the character. The user then inputs an image which is converted to greyscale and the pixel values are turned into an array. The value of each pixel is compared to the ASCII character of the nearest value, then the pixel value is replaced by that ASCII character. The return is a text file where the array of ASCII characters is printed.
