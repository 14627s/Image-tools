import os
from tkinter import filedialog
import time
import cv2

# Function to clear the console screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# ANSI escape codes for colors
class color:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'

clear()

imageselected = None

# Select an image file using tkinter file dialog
while True:
    clear()
    print(f'{color.RED}Selecting image...')
    imageselected = filedialog.askopenfilename()
    if imageselected:
        print(f'{color.GREEN}Image selected: {imageselected}{color.RESET}')
        clear()
        break
    else:
        print(f'{color.RED}No image selected.{color.RESET}')
        time.sleep(2)

# Main menu
print(f'{color.GREEN}   +-+-+-+-+-+ +-+-+-+-+-+\n{color.RED}   |I|M|A|G|E| |T|O|O|L|S|    Github: https://github.com/14627s\n{color.GREEN}   +-+-+-+-+-+ +-+-+-+-+-+\n\n\n[1] Resize Image')
userfirstchoice = input(f'{color.RED}[+] Your choice: ')

if userfirstchoice == '1':
    # Get desired dimensions from user
    width = int(input('[+] Input the width: '))
    height = int(input('[+] Input the height: '))
    print(f'\n [+] Resolution = {width} x {height}')

    # Load and display the selected image using OpenCV
    img = cv2.imread(imageselected)
    resized_img = cv2.resize(img, (width, height))
    cv2.imshow('Resized Image', resized_img)
    cv2.imwrite('resized_image.jpg', resized_img)
    print(f'\n\n{color.GREEN} Image saved successfuly ')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Invalid choice. Exiting...')
