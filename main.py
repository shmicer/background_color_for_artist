
from face_detection import get_avg_color

from PIL import Image, ImageOps, ImageDraw

from pathlib import Path


folder_dir = 'images/artists photo set'
images = Path(folder_dir).glob('*.webp')


# def get_dominant_color():
#     color_thief = ColorThief(image)
#     return color_thief.get_color(quality=1)


def make_image_with_background(img):
    background_image = Image.new('RGB', (1280, 329), color=get_avg_color(image))
    size = img.size
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    output_image = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output_image.putalpha(mask)
    background_image.paste(
        output_image.resize((250, 250)),
        (250, 35),
        mask.resize((250, 250))
    )
    return background_image


for image in images:
    artist_image = Image.open(image)
    make_image_with_background(artist_image).save(f'{image}.png')
    print(get_avg_color(image))



