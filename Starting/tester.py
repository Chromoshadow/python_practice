# from find_ft_type import all_thing_is_obj

# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Toto")

# print(all_thing_is_obj(10))

# --------------------------------------------------------


# from NULL_not_found import NULL_not_found

# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False

# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))


# -----------------------------------------------------------------

# from time import sleep
# from tqdm import tqdm
# from Loading import ft_tqdm

# for elem in ft_tqdm(range(333)):
#     sleep(0.005)
# print()
# for elem in tqdm(range(333)):
#     sleep(0.005)
# print()

# -------------------------------------------------------------------

from ft_package import count_in_list

print(count_in_list.__doc__)

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0