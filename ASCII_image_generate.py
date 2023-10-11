from PIL import Image, ImageDraw, ImageFont
import string

image_width, image_height = 50, 50
font_size = 36
background_color = (255, 255, 255)
font = ImageFont.truetype("C:\Windows\Fonts\Fira Code\CascadiaCode.ttf", font_size)

text_color = (0, 0, 0)

possible_chars = ["0","1","2","3","4","5","6","7","8","9","!","@","#","$",
                  "%","^","&","(",")",":",";","{","}","-","_","+","~","`",
                  "a","b","c","d","e","f","g","h","i","j","k","l","m","n",
                  "o","p","q","r","s","t","u","v","w","x","y","z"]

def character_image_generator(char):
    char_image = Image.new("RGB", (image_width, image_height), background_color)
    draw_char = ImageDraw.Draw(char_image)

    text_width, text_height = draw_char.textsize(char, font=font)
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    draw_char.text((x,y), char, fill=text_color, font=font)
    filename = f"{char}.png"
    char_image.save(filename)

def main():
    for i in possible_chars:
        character_image_generator(i)

if __name__ == "__main__":
    main()