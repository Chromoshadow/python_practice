# from abc import ABC, abstractmethod

# class Character(ABC):
#     """Abstract base character class"""

#     def __init__(self, first_name, is_alive=True):
#         """Initialize the character"""
#         self.first_name = first_name
#         self.is_alive = is_alive

#     @abstractmethod
#     def die(self):
#         """Update the character is_alive status"""
#         self.is_alive = False


# class Stark(Character):
#     """Stark class"""

#     def __init__(self, first_name, is_alive=True):
#         """Initialize the Stark"""
#         self.name = first_name
#         self.is_alive = is_alive

#     def die(self):
#         """Update the Stark is_alive status"""
#         self.is_alive = False

# ----------------------------------------------------------

# from abc import ABC, abstractmethod

# class Character(ABC):
#     """Abstract base character class"""

#     def __init__(self, first_name, family_name, eyes, hairs, is_alive=True):
#         """Initialize the character"""
#         self.first_name = first_name
#         self.is_alive = is_alive
#         self.family_name = family_name
#         self.eyes = eyes
#         self.hairs = hairs

#     @abstractmethod
#     def die(self):
#         """Update the character is_alive status"""
#         self.is_alive = False

#     def __str__(self):
#         return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

#     def __repr__(self):
#         return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


# class Stark(Character):
#     """Representing the Stark family."""

#     def __init__(self, first_name, is_alive=True):
#         """Initialize the Stark"""
#         super().__init__(first_name, "Stark", "grey", "brown", True)

#     def die(self):
#         """Update the Stark is_alive status"""
#         self.is_alive = False


# -----------------------------------------------------------------

from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract base character class"""

    def __init__(self, first_name, family_name, eyes, hairs, is_alive=True):
        """Initialize the character"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs


    @abstractmethod
    def die(self):
        """Update the character is_alive status"""
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def set_eyes(self, color):
        self.eyes = color

    def set_hairs(self, color):
        self.hairs = color

    def get_eyes(self):
        return self.eyes
    
    def get_hairs(self):
        return (self.hairs)



class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the Stark"""
        Character.__init__(self, first_name, "Stark", "grey", "brown", is_alive)

    def die(self):
        """Update the Stark is_alive status"""
        self.is_alive = False

