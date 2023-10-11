import numpy as np
from PIL import Image
import tkinter as tk 
from tkinter import filedialog
from tkinter import ttk
import os

"""
The following section generates an dictionary mapping ASCII values to values between 0 and 255. The values are retrieved from the char_pixel_map.txt file.
"""

file_contents = np.genfromtxt("char_pixel_map.txt", dtype=str, delimiter=' ', comments=None)
for i in range(len(file_contents)):
    file_contents[i][0] = round((int(file_contents[i][0])/317)*255)

ascii_dict = {}
for i in range(len(file_contents)):
    ascii_dict[int(file_contents[i][0])] = file_contents[i][1]

def closest_key(integer):
    key = min(ascii_dict.keys(), key=lambda x: abs(x - integer))
    return ascii_dict[key]

def convert_to_ascii(image_path, output_name):
    """
    This function converts a given image to ASCII characters and outputs a txt file of the image with the name output_name.txt
    """
    global num_of_pixels
    global current_pixel
    image = Image.open(image_path)
    image = image.convert("L")
    pixel_data = np.array(image)
    num_of_pixels = len(pixel_data[0])*len(pixel_data.T[0])

    user_home = os.path.expanduser("~")
    downloads_folder = os.path.join(user_home, "Downloads")

    output_name_ext = f"{output_name}.txt"
    output_path = os.path.join(downloads_folder, output_name_ext)
    
    with open(output_path, 'w') as file:
        current_pixel = 1
        for i in range(len(pixel_data)):
            for j in range(len(pixel_data[0])):
                file.write(f"{closest_key(pixel_data[i][j])}")
                step_val = current_pixel*100/num_of_pixels
                progressbar['value'] = step_val
                window.update()
                current_pixel += 1
            file.write("\n")

    file.close()
    progressbar['value'] -= 0


"""
Here we define functions for buttons in the GUI
"""

def choose_file():
    global selected_file_path
    global current_pixel
    progressbar['value'] = 0
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file_path = file_path
    current_pixel = 0

def convert():
    output_name = output_entry.get()
    if output_name != '':
        convert_to_ascii(selected_file_path, output_name)


"""
Here we setup tkinter
"""

window = tk.Tk()
window.title('Image to ASCII')
window.geometry('820x120')
window.configure(background='#151515')

BUTTON_WIDTH = 12
BUTTON_HEIGHT = 1
BUTTON_FONT = ("Fira Code", 12, "bold")
BUTTON_BG = "#f3c877"
OUTPUT_FONT = ("Fira Code", 8, "normal")


"""
Here we create the buttons and the entry field in the main window.
"""

choose_file_b = tk.Button(window,text="Choose File",command=choose_file,bg=BUTTON_BG,width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT)
choose_file_b.place(x=10,y=10)

output_entry_name = tk.Label(window, text="Output File Name:", bg='#151515', font=OUTPUT_FONT, width=16, height=1, foreground="white")
output_entry_name.place(x=160,y=25)

output_entry = tk.Entry(window, width=60)
output_entry.place(x=290, y=25)

convert_b = tk.Button(window,text="Convert",command=convert,bg=BUTTON_BG,width=BUTTON_WIDTH,height=BUTTON_HEIGHT,font=BUTTON_FONT)
convert_b.place(x=680,y=10)

progressbar = ttk.Progressbar(maximum=100)
progressbar.place(x=30, y=75, width=760)

window.mainloop()