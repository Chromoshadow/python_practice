# from S1E9 import Character


# class Baratheon(Character):
#     """Representing the Baratheon family."""

#     def __init__(self, first_name, is_alive=True):
#         """Initialize the Baratheon"""
#         super().__init__(first_name, "Baratheon", "blue", "black", True)

#     def die(self):
#         """Update the Baratheon is_alive status"""
#         self.is_alive = False


# class Lannister(Character):
#     """Representing the Lannister family."""

#     def __init__(self, first_name, is_alive=True):
#         """Initialize the Lannister"""
#         super().__init__(first_name, "Lannister", "green", "gold", True)

#     def die(self):
#         """Update the Lannister is_alive status"""
#         self.is_alive = False

#     @classmethod
#     def create_lannister(cls, first_name, is_alive=True):
#         return cls(first_name)


# ---------------------------------------------------

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the Baratheon"""
        Character.__init__(self, first_name, "Baratheon", "blue", "black", is_alive)

    def die(self):
        """Update the Baratheon is_alive status"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the Lannister"""
        Character.__init__(self, first_name, "Lannister", "green", "gold", is_alive)

    def die(self):
        """Update the Lannister is_alive status"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
