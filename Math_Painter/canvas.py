import numpy as np
from PIL import Image


class Canvas:
    """
    Object where all the plots will be drawn
    which is a 3d numpy array
    """

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        #create a 3d array
        self.array = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        #assign the user color
        self.array[:] = self.color

    def make(self, filepath):
        """
        Convert teh array into an image and save it
        to the provided filepath
        """
        img = Image.fromarray(self.array, 'RGB')
        img.save(filepath)
