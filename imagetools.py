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
print(f'{color.GREEN}   +-+-+-+-+-+ +-+-+-+-+-+\n{color.RED}   |I|M|A|G|E| |T|O|O|L|S|    Github: https://github.com/14627s\n{color.GREEN}   +-+-+-+-+-+ +-+-+-+-+-+\n\n\n[1] Resize Image\n[2] Image roations & flips\n\n')

userfirstchoice = int(input(f'{color.RED}[+] Your choice: '))

if userfirstchoice == 1:
    # Get desired dimensions from user
    width = int(input('[+] Input the width: '))
    height = int(input('[+] Input the height: '))
    print(f'\n [+] Resolution = {width} x {height}')

    # Load and display the selected image using OpenCV
    img = cv2.imread(imageselected)
    resized_img = cv2.resize(img, (width, height))
    cv2.imshow('Resized Image', resized_img)
    cv2.imwrite('resized_image.jpg', resized_img)
    print(f'\n\n{color.GREEN} Image saved successfully ')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if userfirstchoice == 2:
    clear()
    print(
        f'{color.GREEN}   +-+-+-+-+-+ +-+-+-+-+-+\n{color.RED}   |I|M|A|G|E| |T|O|O|L|S|    Github: https://github.com/14627s\n{color.GREEN}   +-+-+-+-+-+ +-+-+-+-+-+\n\n')
    print(f'{color.GREEN}[1] Right Rotation 90\n[2] Left Rotation 90\n[3] Horizontal FLIP\n[4] Vertical FLIP\n[5] Both FLIP\n')
    userroationchoice = int(input(f'{color.RED}[+] Your choice '))
    if userroationchoice == 1:
        img = cv2.imread(imageselected)
        final_rotated_image  = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotated Image', final_rotated_image)
        cv2.imwrite('resized_image.jpg', final_rotated_image)
        print(f'\n\n{color.GREEN} Image saved successfully ')
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if userroationchoice == 2:
        img = cv2.imread(imageselected)
        final_rotated_image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow('Rotated Image', final_rotated_image)
        cv2.imwrite('resized_image.jpg', final_rotated_image)
        print(f'\n\n{color.GREEN} Image saved successfully ')
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if userroationchoice == 3:
        img = cv2.imread(imageselected)
        final_fliped_image = cv2.flip(img, 1)
        cv2.imshow('Flip Image', final_fliped_image)
        cv2.imwrite('fliped_image.jpg', final_fliped_image)
        print(f'\n\n{color.GREEN} Image saved successfully ')
    if userroationchoice == 4:
        img = cv2.imread(imageselected)
        final_fliped_image = cv2.flip(img, 0)
        cv2.imshow('Flip Image', final_fliped_image)
        cv2.imwrite('fliped_image.jpg', final_fliped_image)
        print(f'\n\n{color.GREEN} Image saved successfully ')
    if userroationchoice == 5:
        img = cv2.imread(imageselected)
        final_fliped_image = cv2.flip(img, -1)
        cv2.imshow('Flip Image', final_fliped_image)
        cv2.imwrite('fliped_image.jpg', final_fliped_image)
        print(f'\n\n{color.GREEN} Image saved successfully ')
else:
    print('Invalid choice. Exiting...')
