
from pathlib import Path
from get_background_color import GetBackgroundColor


directory = 'images/artists photo set'
images = Path(directory).glob('*.webp')



for image in images:
    obj = GetBackgroundColor(image)
    print(obj.get_background_color())
    obj.make_image_with_background().save(f'{image}.png')