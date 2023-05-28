import numpy
import cv2

from PIL import Image, ImageOps, ImageDraw

from pathlib import Path


class GetAverageColor:
    def __init__(self, img, mode='RGB'):

        self.img_str = str(img)
        if mode == 'RGB':
            self.img = Image.open(img)
        elif mode == 'BGR':
            self.img = Image.open(img)[..., ::-1]
        else:
            raise ValueError('Invalid mode. Only RGB and BGR image ' \
                             'mode supported.')

    def get_average_color(self):
        arr_img = cv2.imread(self.img_str)
        avg_color_per_row = numpy.average(arr_img, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        avg_color = tuple([int(i) + 15 for i in avg_color][::-1])
        return '#%02x%02x%02x' % avg_color

    def make_image_with_background(self):
        wrapped_image = Image.new('RGB', (1280, 329), color=self.get_average_color())
        size = self.img.size
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        output_image = ImageOps.fit(self.img, mask.size, centering=(0.5, 0.5))
        output_image.putalpha(mask)
        wrapped_image.paste(
            output_image.resize((250, 250)),
            (250, 35),
            mask.resize((250, 250))
        )
        return wrapped_image


directory = 'images/artists photo set'
images = Path(directory).glob('*.webp')

for image in images:
    obj = GetAverageColor(image)
    print(obj.get_average_color())
    obj.make_image_with_background().save(f'{image}.png')
