from time import sleep
from PIL import Image
import cv2
import pytesseract
import pyautogui
import keyboard


##############
# text = pytesseract.image_to_string(img)
# print(text)
###############

def auto_scr_and_kb():
    """
    Необходима обязательная установка Tesseract и языкового пакета для поддержки языков отличных от EN.
    Последовтельность действий: делает скриншот текущего окна -> обрезает по центру с заданным размером и сохраняет
    в определнной папке -> расподзнаёт текст на русском языке и печатает его управляя клавиатурой.

    :return: печатает распознанный текст управляя клавиатурой
    """
    sleep(10)
    # Обязательно для WIN:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
        """
        Функция для обрезки изображения по центру.
        """
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2 - 150,
                             (img_height + crop_height) // 2))

    pyautogui.screenshot('D:\screen_for_ex.png')
    im = Image.open('D:\screen_for_ex.png')
    img_new = crop_center(im, 1100, 500)
    img_new.save('D:\screen_for_ex.png', quality=95)
    img = cv2.imread('D:\screen_for_ex.png')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
    data = pytesseract.image_to_string(img, lang='rus')
    sleep(1)
    keyboard.write(data.replace('\n', ' '), 0.1)


def text_recognising():
    """
    Распознаёт текст на скрине/картинке
    :return: распознаный текст
    """
    # Обязательно для WIN:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = Image.open('D:\ss.png')
    text = pytesseract.image_to_string(img, lang='rus')
    return text











# Работает:
# sleep(10)
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pyautogui.screenshot('D:\screen_for_ex.png')
# def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
#     """
#     Функция для обрезки изображения по центру.
#     """
#     img_width, img_height = pil_img.size
#     return pil_img.crop(((img_width - crop_width) // 2 ,
#                          (img_height - crop_height) // 2 ,
#                          (img_width + crop_width) // 2 -150,
#                          (img_height + crop_height) // 2))
#
# im = Image.open('D:\screen_for_ex.png')
# im_new = crop_center(im, 1100, 500)
# im_new.save('D:\screen_for_ex.png', quality=95)
#
#
# img = cv2.imread('D:\screen_for_ex.png')
# img = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
# data = pytesseract.image_to_string(img, lang='rus')
# sleep(1)
# print(data.replace('\n',' '))
# # keyboard.write(data.replace('\n',' '), 0.1)

