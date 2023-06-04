import colorsys

import numpy
from PIL import Image
from pathlib import Path
from get_background_color import GetBackgroundColor
from kmeans_clusters_method import ClusterBackgroundColor

directory = 'images/artists photo set/test_images'
images = Path(directory).glob('*.webp')


def get_cluster_color():
    for image in images:
        img = Image.open(image)
        im2arr = numpy.asarray(img)
        obj = ClusterBackgroundColor(im2arr)
        obj.make_image_with_background().save(f'{image}.png')


def get_average_color():
    for image in images:
        obj = GetBackgroundColor(image)
        obj.make_image_with_background().save(f'{image}.png')



# get_cluster_color()
get_average_color()

