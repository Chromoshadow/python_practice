from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Loads a image, prints its format, and return the RGB value
    of every pixel as an numpy array.

    The function verifies that the file exists and that its extension is
    either '.jpg' or '.jpeg'. The image is converted to RGB mode before
    printing its pixel values.

    Args:
        path (str): Path to the image file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: If the file is not a valid image or is corrupted.

    Returns:
        numpy array
    """
    try:
        with Image.open(path).convert("RGB") as img:
            img.verify()
    except FileNotFoundError:
        raise AssertionError(f"Error: file '{path}' not found")
    except Exception:
        raise AssertionError(f"Error: file '{path}' is not an image")

    image_np = np.array(img)
    print(f"The shape of image is: {image_np.shape}")
    return image_np


# NumPy : understand arrays and image representations.
# Pillow : basic image loading and manipulation.
# Matplotlib : visualize images and model outputs.
# OpenCV : image processing and computer vision techniques.
# PyTorch : tensors, datasets, and training pipelines.
# torchvision : transforms, pretrained models, and data loading.
# Hugging Face Transformers : state-of-the-art vision models.
