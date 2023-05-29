import numpy
from PIL import Image
from pathlib import Path
from get_background_color import GetBackgroundColor
from kmeans_clusters_method import SpotifyBackgroundColor


directory = 'images/artists photo set'
images = Path(directory).glob('*.webp')


for image in images:
    img = Image.open(image)
    im2arr = numpy.asarray(img)
    obj = SpotifyBackgroundColor(im2arr)
    obj.make_image_with_background().save(f'{image}.png')


# image = 'images/artists photo set/1.webp'
#
# img_obj = GetBackgroundColor(image)
#
# img = Image.open(image)
# im2arr = numpy.asarray(img)
# img_obj_2 = SpotifyBackgroundColor(im2arr)
#
# print(img_obj.get_background_color())
# print(img_obj_2.best_color())
#
# img_obj.make_image_with_background().save('2.png')




