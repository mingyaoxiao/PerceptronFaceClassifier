import multiprocessing
import imageio
import skimage

# Step One is to downsample the images
## First, lets figure out how to load the images and display them
def get_images_paths():
    paths = []
    paths.append(r"Resources/w1.jpg")
    paths.append(r"Resources/w2.jpg")
    paths.append(r"Resources/w3.jpg")
    paths.append(r"Resources/b1.jpg")
    paths.append(r"Resources/b2.jpg")
    paths.append(r"Resources/b3.jpg")
    return paths

paths = get_images_paths()


# Step Two is to convolve with varying side lengths, and get a vector
# Step Three is to start the learning algorithm

