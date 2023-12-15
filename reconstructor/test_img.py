from PIL import Image, ImageDraw
import numpy as np
from skimage.metrics import structural_similarity
import cv2
import matplotlib.pyplot as plt

class ConstructImage:

    def __init__(self, path_to_your_image, polySize):
        "size is the number of vertice use to make the image (in polygon)"
        self.reference_img = Image.open(path_to_your_image)
        self.polySize = polySize

        self.width, self.height = self.reference_img.size
        self.pixel = self.width * self.height
        self.reference_imgCv2 = self.pil_cv2(self.reference_img)

    def polyDataToImage(self, polyData):
        
        "The polyData parameter is a list where each item represents vertices' locations, color, and transparency for the respective polygon. "

        image = Image.new('RGB', (self.width, self.height))#TODO
        make = ImageDraw.Draw(image, 'RGBA')

        # divide the polyData to chunks, each containing the data for a single poly:
        # x,y each vertex + RGBA
        chunkSize = self.polySize * 2 + 4  
        polys = self.distribute_list(polyData, chunkSize)

        # iterate on the polys and draw 
        for poly in polys:
            index = 0

            # get and put the vertices poly:
            vertices = []
            for vertex in range(self.polySize):
                vertices.append((int(poly[index] * self.width), int(poly[index + 1] * self.height)))
                index += 2

            # get the RGB and alpha values poly:
            red = int(poly[index] * 255)
            green = int(poly[index + 1] * 255)
            blue = int(poly[index + 2] * 255)
            alpha = int(poly[index + 3] * 255)

            # draw to image
            make.polygon(vertices, (red, green, blue, alpha))

        # delete
        del make

        return image

    def MSE_diff(self, polyData, method="MSE"):
        """
       Accepts polygon data, creates an image containing these polygons, 
       and calculates the difference between this image and the reference image 
       using either Mean Squared Error (MSE) or Structural Similarity Index (SSIM).
        """

        # make the image that contains polydata
        image = self.polyDataToImage(polyData)

        if method == "MSE":
            return self.get_mse(image)
        else:
            return 1.0 - self.get_ssim(image)

    def plt_img(self, image, header=None):
        "Creates a side-by-side plot of the given image next to the reference image using matplotlib.pyplot."

        fig = plt.figure("Image Comparison:")
        if header:
            plt.suptitle(header)

        # plot the reference image on the left:
        ax = fig.add_subplot(1, 2, 1)
        plt.imshow(self.reference_img)
        self.ticksOff(plt)

        # plot the given image on the right:
        fig.add_subplot(1, 2, 2)
        plt.imshow(image)
        self.ticksOff(plt)

        return plt

    def save_img(self, polyData, imageFilePath, header=None):
        "Accepts polygon data, creates an image containing these polygons, creates a side-by-side plot, and saves the plot to a file."

        # create the image
        image = self.polyDataToImage(polyData)

        # to plot it side by side
        self.plt_img(image, header)

        # save to file
        plt.savefig(imageFilePath)

    # other in file methods:

    def pil_cv2(self, pil_image):
        "pillow to CV2 format"
        return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    def get_mse(self, image):
        "count the diff of MSE between the reference and created image"
        return np.sum((self.pil_cv2(image).astype("float") - self.reference_imgCv2.astype("float")) ** 2)/float(self.pixel)

    def get_ssim(self, image):
        "count the diff of SSIM between the ref and creaetd image"
        return structural_similarity(self.pil_cv2(image), self.reference_imgCv2, multichannel=True)

    def distribute_list(self, list, chunkSize):
        "distribute the list to chunk"
        for chunk in range(0, len(list), chunkSize):
            yield(list[chunk:chunk + chunkSize])

    def ticksOff(self, plot):#TODO
        "turns off ticks on both axes"
        plt.tick_params(
            axis='both',
            which='both',
            bottom=False,
            left=False,
            top=False,
            right=False,
            labelbottom=False,
            labelleft=False,
        )
