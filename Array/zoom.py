import argparse
from PIL import Image
import numpy as np
from load_image import ft_load


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    img = ft_load(args.path)
    print(img)
    sliced = img[100:500, 450:850]
    zoom = Image.fromarray(sliced).convert("L")
    print(f"New shape after slicing: {np.array(zoom).shape}")
    zoom.show()
    print(sliced)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
