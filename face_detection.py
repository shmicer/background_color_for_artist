
import cv2
import numpy
from PIL import Image
from pathlib import Path

folder_dir = 'images/artists photo set'
images = Path(folder_dir).glob('*.webp')


def get_avg_color(img):
    myimg = cv2.imread(str(img))
    avg_color_per_row = numpy.average(myimg, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    avg_color = tuple([int(i) for i in avg_color][::-1])
    # first_color = tuple(avg_color)
    # second_color = tuple(i + 15 for i in avg_color[:2] + avg_color[2:])
    return avg_color




# def face_detection():
#     for img in images:
#         face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
#         temp_img = cv2.imread(str(img))
#         gray = cv2.cvtColor(temp_img, cv2.COLOR_BGR2GRAY)
#
#         faces = face_cascade.detectMultiScale(gray, 1.1, 5)
#
#         for (x, y, w, h) in faces:
#             cv2.rectangle(temp_img, (x, y), (int(0.9 *(x + w)), int(y + h * 0.9)), (255, 255, 255), -1)
#             cv2.imwrite(f'{img}.webp', temp_img)
#         print('add')


