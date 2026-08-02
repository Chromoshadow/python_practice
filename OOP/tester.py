# from S1E9 import Character, Stark

# Ned = Stark("Ned")
# print(Ned.__dict__)
# print(Ned.is_alive)
# Ned.die()
# print(Ned.is_alive)
# print(Ned.__doc__)
# print(Ned.__init__.__doc__)
# print(Ned.die.__doc__)
# print("---")
# Lyanna = Stark("Lyanna", False)
# print(Lyanna.__dict__)


# from S1E9 import Character
# hodor = Character("hodor")


# -------------------------------------------------


# from S1E7 import Baratheon, Lannister

# Robert = Baratheon("Robert")
# print(Robert.__dict__)
# print(Robert.__str__)
# print(Robert.__repr__)
# print(Robert.is_alive)
# Robert.die()
# print(Robert.is_alive)
# print(Robert.__doc__)
# print("---")
# Cersei = Lannister("Cersei")
# print(Cersei.__dict__)
# print(Cersei.__str__)
# print(Cersei.is_alive)
# print("---")
# Jaime = Lannister.create_lannister("Jaime", True)
# print(f"Name : {Jaime.first_name, type(Jaime).__name__}, Alive : {Jaime.is_alive}")


# ----------------------------------------------------


# from DiamondTrap import King

# Joffrey = King("Joffrey")
# print(Joffrey.__dict__)
# Joffrey.set_eyes("green")
# Joffrey.set_hairs("gold")
# print(Joffrey.get_eyes())
# print(Joffrey.get_hairs())
# print(Joffrey.__dict__)


# ---------------------------------------------------------

# from ft_calculator import calculator

# v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v1 + 5
# print("---")
# v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v2 * 5
# print("---")
# v3 = calculator([10.0, 15.0, 20.0])
# v3 - 5
# v3 / 5

# ----------------------------------------------------------

from ft_calculator import calculator
a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)
