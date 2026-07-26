from numpy import array as array
from PIL import Image


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    array[:, :, 0] = 255 - array[:, :, 0]
    array[:, :, 1] = 255 - array[:, :, 1]
    array[:, :, 2] = 255 - array[:, :, 2]
    print(array)
    Image.fromarray(array).show()
    return array


def ft_red(array) -> array:
    """Apply a red filter to the image received."""
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    Image.fromarray(array).show()
    return array


def ft_green(array) -> array:
    """Apply a green filter to the image received."""
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    Image.fromarray(array).show()
    return array


def ft_blue(array) -> array:
    """Apply a blue filter to the image received."""
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    Image.fromarray(array).show()
    return array


def ft_grey(array) -> array:
    """Apply a grey filter to the image received."""
    array[:, :, 0] = array[:, :, 1] = array[:, :, 2]
    Image.fromarray(array).show()
    return array
