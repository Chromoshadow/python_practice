# from give_bmi import give_bmi, apply_limit

# height = [2.71, 1.15]
# weight = [165.3, 38.4]

# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))

# ------------------------------------------------

# from array2D import slice_me

# family = [[1.80, 78.4],
#           [2.15, 102.7],
#           [2.10, 98.5],
#           [1.88, 75.2]]

# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))

# -----------------------------------------------------

# from load_image import ft_load

# print(ft_load("landscape.jpg"))


# --------------------------------------------------------

from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey

array = ft_load("landscape.jpg")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)
