import numpy
import cv2

import colorsys
from PIL import Image, ImageOps, ImageDraw


class GetBackgroundColor:
    def __init__(self, img, mode='RGB'):

        self.img_str = str(img)
        if mode == 'RGB':
            self.img = Image.open(img)
        elif mode == 'BGR':
            self.img = Image.open(img)[..., ::-1]
        else:
            raise ValueError('Invalid mode. Only RGB and BGR image '\
                             'mode supported.')

    def get_background_color(self):
        arr_img = cv2.imread(self.img_str)
        avg_color_per_row = numpy.average(arr_img, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        avg_color = tuple([int(i) for i in avg_color][::-1])
        # return '#%02x%02x%02x' % avg_color
        return avg_color

    def rgb_to_hsv(self):
        (r, g, b) = self.get_background_color()
        # normalize
        (r, g, b) = (r / 255, g / 255, b / 255)
        # convert to hsv
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        # expand HSV range
        (h, s, v) = (int(h * 255), (int(s * 255 * 1.4) if (s * 255) < 60 else int(s * 255)), (int(v * 255) if (v * 255) > 60 else 60))
        # (h, s, v) = (int(h * 255), int(s * 255), int(v * 255))
        return h, s, v

    def make_image_with_background(self, size=(1280, 329)):
        wrapped_image = Image.new('HSV', size, color=self.rgb_to_hsv())
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

