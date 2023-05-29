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





