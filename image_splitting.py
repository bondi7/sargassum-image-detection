import numpy as np


def split_image(image, num_images, verbose=False):
    """
    Splits an image (ndarray) into 'num_images' images and returns the splitted
    images

    Parameters:
    -----------
    'image': numpy ndarray
        'image' must be a squared 2D numpy array 

    'num_images': int
        indicates the number of images to be returned

    Returns:
    --------
    'splitted_images': numpy ndarray
    """
    (width, height, rgb) = image.shape
    if width != height: raise Exception('image must be a squared ndarray')
    num_windows = int(np.sqrt(num_images))
    window_size = width // num_windows
    if verbose:
        print(f"\tImage of size ({width}x{height}). Window size: {window_size}")
    splitted_images = []
    y = 0
    while (y+window_size <= height):
        x = 0
        while (x+window_size <= width):
            if verbose: print(f"\t({x},{x+window_size}:{y},{y+window_size})\t", end='')
            splitted_images.append(image[x:x+window_size, y:y+window_size])
            x += window_size
        if verbose: print()
        y += window_size
    return np.array(splitted_images)
